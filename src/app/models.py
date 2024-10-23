from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str | None]
    price: Mapped[float]
    stock_quantity: Mapped[int]
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))


class Category(Base):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(unique=True)

    products: Mapped[list["Product"]] = relationship(lazy="selectin")
