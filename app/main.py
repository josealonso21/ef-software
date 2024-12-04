from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_db
from .crud import get_ticket_by_id, update_ticket_status
from .schemas import TicketResponse

app = FastAPI()

@app.get("/tickets/{ticket_id}", response_model=TicketResponse)
async def read_ticket(ticket_id: int, db: AsyncSession = Depends(get_db)):
    ticket = await get_ticket_by_id(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@app.post("/tickets/{ticket_id}/reserve")
async def reserve_ticket(ticket_id: int, db: AsyncSession = Depends(get_db)):
    ticket = await update_ticket_status(db, ticket_id, "reserved")
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"message": "Ticket reserved successfully"}
