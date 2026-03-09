from fastapi import APIRouter, HTTPException

from src.core.utils import pydantic_to_base64, get_signed_api_sign
from src.api.v1.deps import TransactionServiceDep
from src.schemas.search import SearchParamsSchema
from src.schemas.transaction import TransactionsData
from src.api.v1.schemas import SignedApiData


messages_router = APIRouter(prefix='/api/messages', tags=['messages'])


@messages_router.post('/outgoing', response_model=SignedApiData)
async def outgoing(data: SignedApiData, service: TransactionServiceDep):
    
    expected_sign = get_signed_api_sign(data.Data)
    if not data.Sign or data.Sign != expected_sign:
        raise HTTPException(status_code=400, detail='Invalid request signature')
    
    try:
        search_params = SearchParamsSchema.model_validate_json(data.Data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    transactions = await service.search_transactions(search_params)

    response_data = TransactionsData(Transactions=transactions, Count=len(transactions))
    response_data_b64 = pydantic_to_base64(response_data)
    response_sign = get_signed_api_sign(response_data_b64)
    
    return SignedApiData(Data=response_data_b64, Sign=response_sign, SignerCert='SignerCert')


@messages_router.post('/incoming')
async def incoming(data: SignedApiData, service: TransactionServiceDep):
    
    expected_sign = get_signed_api_sign(data.Data)
    if not data.Sign or data.Sign != expected_sign:
        raise HTTPException(status_code=400, detail='Invalid request signature')
    
    try:
        transactions = TransactionsData.model_validate_json(data.Data)
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))
    
    try:
        receipt_transactions = await service.save_transactions(transactions.Transactions)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        
    response_data = TransactionsData(
        Transactions=receipt_transactions,
        Count=len(receipt_transactions),
    )
    response_data_b64 = pydantic_to_base64(response_data)
    response_sign = get_signed_api_sign(response_data_b64)
    return SignedApiData(Data=response_data_b64, Sign=response_sign, SignerCert='SignerCert')


