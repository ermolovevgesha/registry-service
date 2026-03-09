import base64
import hashlib

from pydantic import BaseModel


def encode64(data: bytes) -> str:
    return base64.b64encode(data).decode()


def decode64(data: str) -> bytes:
    return base64.b64decode(data)


def get_hash(data_dict: bytes) -> str:
    hash_object = hashlib.sha256(data_dict)
    return hash_object.hexdigest().upper()


def pydantic_to_base64(schema: BaseModel):
    return encode64(schema.model_dump_json().encode())


def get_transaction_sign_from_hash(hash: str) -> str:
    return encode64(hash.encode())


def get_signed_api_sign(data_b64: str) -> str:
    hash = get_hash(data_b64.encode()).encode()
    
    return encode64(hash)

