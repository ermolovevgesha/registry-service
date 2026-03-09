from typing import Optional

from pydantic import BaseModel, Base64Str


class SignedApiData(BaseModel):
    Data: Base64Str = 'eyJTdGFydERhdGUiOiAiMjAyNC0wMS0wMVQwMDowMDowMFoiLCAiRW5kRGF0ZSI6ICIyMDI2LTEyLTMxVDIzOjU5OjU5WiIsICJMaW1pdCI6IDEwLCAiT2Zmc2V0IjogMH0='
    Sign: Optional[str] = 'MTlGOEI3QTJDOEE3NDAzNUJERTBBRjRCMTY1MjIzNDREREIyM0E1ODVBRTdEMjFEQjQ4N0ZBNTdGNkEyRjM3Ng=='
    SignerCert: Optional[str] = None
    
