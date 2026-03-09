from datetime import datetime

from pydantic import BaseModel


class SearchParamsSchema(BaseModel):
    StartDate: datetime
    EndDate: datetime
    Limit: int
    Offset: int
    
