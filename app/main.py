from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_db
from .crud import (
    get_ticket_by_id,
    buy_ticket,
    reserve_ticket,
    cancel_reservation,
)
from .schemas import TicketResponse

app = FastAPI()

@app.get("/tickets/{ticket_id}", response_model=TicketResponse)
async def read_ticket(ticket_id: int, db: AsyncSession = Depends(get_db)):
    ticket = await get_ticket_by_id(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@app.post("/tickets/{ticket_id}/reserve")
async def reserve_ticket_endpoint(ticket_id: int, user_id: int, db: AsyncSession = Depends(get_db)):
    ticket = await reserve_ticket(db, ticket_id, user_id)
    if not ticket:
        raise HTTPException(status_code=400, detail="Unable to reserve ticket")
    return {"message": "Ticket reserved successfully"}

@app.post("/tickets/{ticket_id}/buy")
async def buy_ticket_endpoint(ticket_id: int, user_id: int, db: AsyncSession = Depends(get_db)):
    ticket = await buy_ticket(db, ticket_id, user_id)
    if not ticket:
        raise HTTPException(status_code=400, detail="Unable to buy ticket")
    return {"message": "Ticket purchased successfully"}

@app.post("/tickets/{ticket_id}/cancel")
async def cancel_ticket_endpoint(ticket_id: int, db: AsyncSession = Depends(get_db)):
    ticket = await cancel_reservation(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=400, detail="Unable to cancel ticket")
    return {"message": "Ticket reservation canceled"}