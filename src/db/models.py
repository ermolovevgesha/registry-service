from typing import Optional
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.db.database import Base


class TransactionModel(Base):
    __tablename__ = "transactions"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    TransactionType: Mapped[int]
    Data: Mapped[str]
    Hash: Mapped[str]
    Sign: Mapped[str]
    SignerCert: Mapped[str]
    TransactionTime: Mapped[datetime]
    Metadata: Mapped[str] = mapped_column(nullable=True)
    TransactionIn: Mapped[Optional[str]] 
    TransactionOut: Mapped[Optional[str]]
    