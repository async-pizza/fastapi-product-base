import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.testclient import TestClient

from app.models import Category, Product


async def test_create_product(
    client: "TestClient", category: "Category"
) -> None:
    data = {
        "name": "test_product",
        "description": None,
        "price": 100.0,
        "stock_quantity": 10,
        "category_id": category.id,
    }
    response = client.post("/api/products/", json=data)
    assert response.status_code == status.HTTP_201_CREATED
    response_data = response.json()
    data["id"] = response_data["id"]
    assert response_data == data


@pytest.mark.usefixtures("product")
async def test_create_product_already_exists(
    client: "TestClient", category: "Category"
) -> None:
    data = {
        "name": "test_product",
        "description": None,
        "price": 100.0,
        "stock_quantity": 10,
        "category_id": category.id,
    }
    response = client.post("/api/products/", json=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "Product already exists"}


async def test_get_products(client: "TestClient", product: "Product") -> None:
    response = client.get("/api/products/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock_quantity": product.stock_quantity,
            "category_id": product.category_id,
        }
    ]


async def test_delete_product(
    client: "TestClient", product: "Product", session: "AsyncSession"
) -> None:
    response = client.delete(f"/api/products/{product.id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db_products = await Product.all(session=session)
    assert db_products == []
