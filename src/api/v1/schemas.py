from typing import Optional
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SignedApiData(BaseModel):
    Data: str
    Sign: Optional[str] = None
    SignerCert: Optional[str] = None
    
class SearchRequest(BaseModel):
    StartDate: datetime
    EndDate: datetime
    Limit: int
    Offset: int
    
class Transaction(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    TransactionType: int
    Data: str
    Hash: str
    Sign: str
    SignerCert: str
    TransactionTime: datetime
    Metadata: Optional[str]
    TransactionIn: Optional[str]
    TransactionOut: Optional[str]
    
class TransactionsData(BaseModel):
    Transactions: list[Transaction]
    Count: int
    
