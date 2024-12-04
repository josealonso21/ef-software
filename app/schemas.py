from pydantic import BaseModel

class TicketBase(BaseModel):
    event_name: str
    status: str

class TicketCreate(TicketBase):
    pass

class TicketUpdate(TicketBase):
    status: str

class TicketResponse(TicketBase):
    id: int

    class Config:
        orm_mode = True