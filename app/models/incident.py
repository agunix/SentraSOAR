from pydantic import BaseModel
from datetime import datetime

class Incident(BaseModel):
    id: int
    title: str
    severity: str
    source_ip: str
    created_at: datetime
    status: str = "open"