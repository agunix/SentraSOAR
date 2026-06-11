from pydantic import BaseModel

class Alert(BaseModel):
    name: str
    severity: str
    source_ip: str
    details: dict