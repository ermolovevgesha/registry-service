import asyncio

from alembic import command
from alembic.config import Config

from src.db.database import async_session_maker
from src.db.test_data import get_outgoing_test_data
from src.db.repositories import TransactionRepository

async def init_db():
    alembic_cfg = Config("alembic.ini")
    await asyncio.to_thread(command.upgrade, alembic_cfg, "head")
    
    async with async_session_maker() as session:
        trans_repo = TransactionRepository(session)
        await trans_repo.save(get_outgoing_test_data())
        await trans_repo.commit()
        
