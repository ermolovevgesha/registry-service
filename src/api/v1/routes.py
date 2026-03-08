from fastapi import APIRouter, Depends

from src.api.v1.deps import SessionDep
from src.api.v1.schemas import SignedApiData, SearchRequest, Transaction, TransactionsData
from src.api.v1.services import APIService
from src.core.utils import decode, encode

from src.core.test_data import init_outgoing_test_data


messages_router = APIRouter(prefix='/api/messages', tags=['messages'])

service = APIService()


@messages_router.post('/outgoing', response_model=SignedApiData)
async def outgoing(data: SignedApiData, session: SessionDep):
    decoded_data = SearchRequest.model_validate_json(decode(data.Data))
    
    db_transactions = await service.search_transactions(decoded_data.StartDate, decoded_data.EndDate, decoded_data.Limit, decoded_data.Offset, session)

    transactions_list = [Transaction.model_validate(t) for t in db_transactions]
    
    trans_data = TransactionsData(Transactions=transactions_list, Count=len(transactions_list))
    
    return SignedApiData(Data=encode(trans_data.model_dump_json().encode()))

