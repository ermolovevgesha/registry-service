from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.database import get_async_session
from src.api.v1.services import TransactionService
from src.db.repositories import TransactionRepository


SessionDep = Annotated[AsyncSession, Depends(get_async_session)]

def get_api_service(session: SessionDep):
    transactions_repo = TransactionRepository(session)
    return TransactionService(transactions_repo)

TransactionServiceDep = Annotated[TransactionService, Depends(get_api_service)]


