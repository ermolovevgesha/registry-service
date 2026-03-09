from typing import Optional
from datetime import datetime
from typing_extensions import Self

from pydantic import BaseModel, ConfigDict, model_validator, Base64Str

from src.core.utils import get_hash


class Transaction(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    TransactionType: int
    Data: Base64Str
    Hash: str
    Sign: str
    SignerCert: str
    TransactionTime: datetime
    Metadata: Optional[str] = None
    TransactionIn: Optional[str] = None
    TransactionOut: Optional[str] = None


class TransactionValid(Transaction):
    @model_validator(mode='after')
    def check_hash_match(self) -> Self:
        if self.Hash != get_hash(self.model_dump_json(exclude={'Hash', 'Sign'}).encode()):
            raise ValueError('Hash mismatch for transaction')
        return self


class TransactionsData(BaseModel):
    Transactions: list[Transaction]
    Count: int
    
