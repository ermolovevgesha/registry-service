from typing import AsyncGenerator

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.core.config import settings


async_engine = create_async_engine(url=settings.DATABASE_URL)
sync_engine = create_engine(url=settings.DATABASE_URL)

async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


class Base(DeclarativeBase):
    pass

