from pydantic import BaseModel
from datetime import datetime

class TicketBase(BaseModel):
    event_name: str
    customer_name: str
    status: str

class TicketCreate(TicketBase):
    pass

class TicketResponse(TicketBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True