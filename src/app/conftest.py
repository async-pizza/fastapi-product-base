from typing import AsyncGenerator

import pytest
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
from starlette.testclient import TestClient

from app.database import Base
from app.database.database import engine
from app.models import Category, Product
from main import app


@pytest.fixture(autouse=True)
async def _init_db() -> AsyncGenerator[None, None]:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture()
def client() -> "TestClient":
    return TestClient(app)


@pytest.fixture()
async def session() -> AsyncGenerator["AsyncSession", None]:
    async with AsyncSession(bind=engine, expire_on_commit=False) as session:
        yield session


@pytest.fixture()
async def category(session: "AsyncSession") -> "Category":
    return await Category.create(session, name="food")


@pytest.fixture()
async def product(session: "AsyncSession", category: "Category") -> "Product":
    return await Product.create(
        session,
        name="test_product",
        price=100.0,
        stock_quantity=10,
        category_id=category.id,
    )
