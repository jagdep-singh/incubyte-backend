from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Sweet(Base):
    __tablename__ = "sweets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)
    category: Mapped[str]
    price: Mapped[float]
    quantity: Mapped[int]
