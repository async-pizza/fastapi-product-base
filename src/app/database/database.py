from typing import AsyncGenerator, ParamSpec, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from settings import config

engine = create_async_engine(config.DATABASE_URL)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(bind=engine, expire_on_commit=False) as session:
        yield session
