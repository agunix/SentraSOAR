from pydantic import BaseModel

class Event(BaseModel):
    source_ip: str
    event_type: str
    username: str | None = None
    status: str