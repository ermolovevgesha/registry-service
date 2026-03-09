from fastapi import APIRouter, HTTPException

from src.core.utils import pydantic_to_base64
from src.api.v1.deps import TransactionServiceDep
from src.schemas.search import SearchParamsSchema
from src.schemas.transaction import TransactionsData
from src.api.v1.schemas import SignedApiData


messages_router = APIRouter(prefix='/api/messages', tags=['messages'])


@messages_router.post('/outgoing', response_model=SignedApiData)
async def outgoing(data: SignedApiData, service: TransactionServiceDep):
    
    transactions = await service.search_transactions(SearchParamsSchema.model_validate_json(data.Data))

    response_data = TransactionsData(Transactions=transactions, Count=len(transactions))

    return SignedApiData(Data=pydantic_to_base64(response_data))


@messages_router.post('/incoming')
async def incoming(data: SignedApiData, service: TransactionServiceDep):
    try:
        transactions = TransactionsData.model_validate_json(data.Data)
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))
    
    receipt_transactions = await service.save_transactions(transactions.Transactions)
        
    response_data = TransactionsData(Transactions=receipt_transactions, Count=len(receipt_transactions))
    return SignedApiData(Data=pydantic_to_base64(response_data))


