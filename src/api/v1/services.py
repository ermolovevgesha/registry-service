from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models import TransactionModel


class APIService():
    async def search_transactions(self, start, end, limit, offset, session: AsyncSession):

        stmt = (
            select(TransactionModel)
            .where(TransactionModel.Metadata == "SYSTEM_A")
            .where(TransactionModel.TransactionTime >= start)
            .where(TransactionModel.TransactionTime <= end)
            .offset(offset)
            .limit(limit)
        )
        
        result = await session.execute(stmt)
        transactions = result.scalars().all()
        
        return transactions
