from datetime import datetime, timezone

from src.db.test_data import get_outgoing_test_data
from src.db.repositories import TransactionRepository
from src.schemas.search import SearchParamsSchema
from src.schemas.transaction import Transaction, TransactionValid
from src.schemas.message import Message, MessageData202, MessageData203, MessageData215
from src.core.utils import pydantic_to_base64, encode64, get_hash, get_transaction_sign_from_hash


class TransactionService():
    def __init__(self, transactions_repo: TransactionRepository):
        self.transactions_repo = transactions_repo
    
    async def create_first_trans(self):
        transaction = get_outgoing_test_data()
        await self.transactions_repo.save(transaction)
        await self.transactions_repo.commit()
        
    async def search_transactions(self, search_params: SearchParamsSchema) -> list[Transaction]:
        return await self.transactions_repo.search(search_params)
    
    
    async def save_transactions(self, transactions: list[Transaction]):
        receipt_transactions = []
    
        for trans in transactions:
            try:
                valid_trans = TransactionValid.model_validate(trans.model_dump())
            except:
                continue
            
            message = Message.model_validate_json(valid_trans.Data)
            
            transaction_to_save = Transaction(
                Metadata=message.ReceiverBranch,
                **valid_trans.model_dump(exclude={'Metadata'})
            )
            
            await self.transactions_repo.save(transaction_to_save)
            
            if message.InfoMessageType == 215: continue
            
            elif message.InfoMessageType == 202:
                payload = MessageData202.model_validate_json(message.Data)
            elif message.InfoMessageType == 203:
                payload = MessageData203.model_validate_json(message.Data)
            else:
                continue
            
            receipt_message = Message(
                Data=pydantic_to_base64(MessageData215(BankGuaranteeHash=payload.BankGuaranteeHash)),
                InfoMessageType=215, 
                SenderBranch='SYSTEM_B', 
                ReceiverBranch='SYSTEM_A', 
                ChainGuid=message.ChainGuid, 
                MessageTime=datetime.now(timezone.utc)
            )
            new_transaction = Transaction(
                TransactionType=9,
                Data=pydantic_to_base64(receipt_message),
                Hash='',
                Sign='',
                TransactionTime=datetime.now(timezone.utc),
                SignerCert=encode64(b'SYSTEM_B_CERT'),
                Metadata=None,
                TransactionIn=None,
                TransactionOut=None
            )
            
            new_transaction_hash = get_hash(new_transaction.model_dump_json(exclude={'Hash', 'Sign'}).encode())
            new_transaction.Hash, new_transaction.Sign = new_transaction_hash, encode64(new_transaction_hash.encode())
            new_transaction.Sign = get_transaction_sign_from_hash(new_transaction_hash)
            receipt_transactions.append(new_transaction)

        await self.transactions_repo.commit()
        
        return receipt_transactions

