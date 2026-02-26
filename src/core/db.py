from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from typing import AsyncGenerator

from src.core.config import settings
from src.db.base import Base

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
)

async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

async def init_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)