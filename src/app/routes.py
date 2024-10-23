import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_session
from app.models import Category, Product
from app.schema import (
    CategoryInSchema,
    CategorySchema,
    ProductInSchema,
    ProductSchema,
)

logger = logging.getLogger(__name__)
app = APIRouter(prefix="/api", tags=["API"])


@app.post("/products/", status_code=201, response_model=ProductSchema)
async def create_product(
    product_data: ProductInSchema,
    session: "AsyncSession" = Depends(get_session),
) -> "Product":
    await Category.get(product_data.category_id, session)
    product = await Product.first_or_none(
        session, Product.name == product_data.name
    )
    if product:
        raise HTTPException(status_code=400, detail="Product already exists")
    return await Product.create(session, **product_data.model_dump())


@app.get("/products/", response_model=list[ProductSchema])
async def get_products(
    session: "AsyncSession" = Depends(get_session),
) -> list["Product"]:
    return await Product.all(session)


@app.delete("/products/{product_id}/", status_code=204)
async def delete_product(
    product_id: int, session: "AsyncSession" = Depends(get_session)
) -> None:
    product = await Product.get(product_id, session)
    await product.delete(session)


@app.put("/products/{product_id}/", response_model=ProductSchema)
async def update_product(
    product_id: int,
    product_data: ProductInSchema,
    session: "AsyncSession" = Depends(get_session),
) -> "Product":
    product = await Product.get(product_id, session)
    await Category.get(product_data.category_id, session)
    return await product.update(session, **product_data.model_dump())


@app.get(
    "/categories/{category_id}/products/", response_model=list[ProductSchema]
)
async def get_products_by_category(
    category_id: int,
    session: "AsyncSession" = Depends(get_session),
) -> list["Product"]:
    category = await Category.get(category_id, session)
    return category.products


@app.get("/categories/", response_model=list[CategorySchema])
async def get_categories(
    session: "AsyncSession" = Depends(get_session),
) -> list["Category"]:
    return await Category.all(session)


@app.post("/categories/", status_code=201, response_model=CategorySchema)
async def create_category(
    category_data: CategoryInSchema,
    session: "AsyncSession" = Depends(get_session),
) -> "Category":
    category = await Category.first_or_none(
        session, Category.name == category_data.name
    )
    if category:
        raise HTTPException(status_code=400, detail="Category already exists")
    return await Category.create(session, **category_data.model_dump())
