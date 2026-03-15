import json
from datetime import datetime, timezone

from src.schemas.transaction import Transaction
from src.core.utils import encode64, get_hash


def get_outgoing_test_data() -> Transaction:
    guarantee = {
        "InformationType": 201,
        "InformationTypeString": "Выдача гарантии",
        "Number": "BG-2024-001",
        "IssuedDate": "2024-05-20T10:00:00Z",
        "Guarantor": "ООО 'Финансовая гарантия'",
        "Beneficiary": "Государственное учреждение 'Получатель'",
        "Principal": "ООО 'Должник'",
        "Obligations": [
            {
                "Type": 1,
                "StartDate": "2024-06-01T00:00:00Z",
                "EndDate": "2024-12-01T00:00:00Z",
                "ActDate": "2024-05-15T00:00:00Z",
                "ActNumber": "ПР-2024/05/15-001",
                "Taxs": [
                    {
                        "Number": "1",
                        "NameTax": "Обязательство по контракту №К-2024-01",
                        "Amount": 50000.00,
                        "PennyAmount": 0.00
                    },
                    {
                        "Number": "2",
                        "NameTax": "Гарантийное обеспечение",
                        "Amount": 15000.00,
                        "PennyAmount": 500.00
                    }
                ]
            }
        ],
        "StartDate": "2024-06-01T00:00:00",
        "EndDate": "2024-12-15T00:00:00",
        "CurrencyCode": "USD",
        "CurrencyName": "Доллар США",
        "Amoun": 65000.00,
        "RevokationInfo": "Безотзывная",
        "ClaimRightTransfer": "Не допускается",
        "PaymentPeriod": "5 рабочих дней с момента получения требования",
        "SignerName": "Иванов Иван Иванович",
        "AuthorizedPosition": "Генеральный директор",
        "BankGuaranteeHash": "5D6F8E2A1C3B9F4D7E8A2C5B1D3F6E8A9C2D4F6A8B1C3E5F7A9D2B4C6E8F0A1"
    }
    guarantee_json = json.dumps(guarantee)
    guarantee_b64 = encode64(guarantee_json.encode())

    message = {
        "Data": guarantee_b64, 
        "SenderBranch": "SYSTEM_B",
        "ReceiverBranch": "SYSTEM_A",
        "InfoMessageType": 201,
        "MessageTime": "2024-05-20T10:05:00Z",
        "ChainGuid": "550e8400-e29b-41d4-a716-446655440000"
    }
    message_json = json.dumps(message)
    message_b64 = encode64(message_json.encode())

    tx_for_hash = {
        "TransactionType": 9,
        "Data": message_b64,
        "Metadata": "Initial Test Data",
        "TransactionTime": "2024-02-20T10:10:00Z",
        "Sign": "",
        "SignerCert": "",
        "Hash": None,
        "TransactionIn": None,
        "TransactionOut": None
    }
    sample_hash = get_hash(json.dumps(tx_for_hash).encode())
    sample_sign = encode64(sample_hash.encode())

    transaction = Transaction(
        TransactionType=10,
        Data=message_b64,
        Hash=sample_hash,
        Sign=sample_sign,
        SignerCert=encode64(b"SYSTEM_B"),
        TransactionTime=datetime.now(timezone.utc),
        Metadata="SYSTEM_A",
    )
    
    return transaction

