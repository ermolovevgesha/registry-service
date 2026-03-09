from uuid import UUID
from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Base64Str


class Message(BaseModel):
    Data: Base64Str
    SenderBranch: str
    ReceiverBranch: str
    InfoMessageType: int
    MessageTime: datetime
    ChainGuid: UUID
    PreviousTransactionHash: Optional[str] = None
    Metadata: Optional[str] = None
    

class MessageData215(BaseModel):
    BankGuaranteeHash: str

    
class MessageData203(BaseModel):
    Name: str
    BankGuaranteeHash: str
    Sign: Base64Str
    SignerCert: Base64Str
    Reason: str

    
class MessageData202(BaseModel):
    Name: str
    BankGuaranteeHash: str
    Sign: Base64Str
    SignerCert: Base64Str
    
    