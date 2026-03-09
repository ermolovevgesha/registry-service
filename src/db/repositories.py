from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models import TransactionModel
from src.schemas.transaction import Transaction
from src.schemas.search import SearchParamsSchema


class TransactionRepository():
    def __init__(self, session: AsyncSession):
        self.session = session
        
        
    async def search(self, search_params: SearchParamsSchema) -> list[Transaction]:
        stmt = (
            select(TransactionModel)
            .where(TransactionModel.Metadata == "SYSTEM_A")
            .where(TransactionModel.TransactionTime >= search_params.StartDate)
            .where(TransactionModel.TransactionTime <= search_params.EndDate)
            .offset(search_params.Offset)
            .limit(search_params.Limit)
        )
        
        result = await self.session.execute(stmt)
        
        transactions = result.scalars().all()
        transactions_list = [Transaction.model_validate(t) for t in transactions]
        return transactions_list
    
    
    async def save(self, transaction: Transaction) -> Transaction:
        db_transaction = TransactionModel(**transaction.model_dump())
        self.session.add(db_transaction)
                
        return Transaction.model_validate(db_transaction)
    
    
    async def commit(self):
        await self.session.commit()
    
