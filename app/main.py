from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_db
from .crud import get_ticket_by_id, buy_ticket, reserve_ticket, cancel_reservation
from .schemas import TicketResponse

import logging
from datetime import datetime

# Configuración de logs
log_filename = f"./logs/log_{datetime.now().strftime('%d_%m_%Y')}.log"
logging.basicConfig(filename=log_filename, level=logging.INFO)

app = FastAPI()

@app.get("/tickets/{ticket_id}", response_model=TicketResponse)
async def read_ticket(ticket_id: int, db: AsyncSession = Depends(get_db)):
    ticket = await get_ticket_by_id(db, ticket_id)
    if not ticket:
        logging.error("Error en Ejecución: Ticket no encontrado")
        raise HTTPException(status_code=404, detail="Ticket not found")
    logging.info("Éxito en Ejecución: Ticket encontrado")
    return ticket

@app.post("/tickets/{ticket_id}/reserve")
async def reserve_ticket_endpoint(ticket_id: int, user_id: int, db: AsyncSession = Depends(get_db)):
    ticket = await reserve_ticket(db, ticket_id, user_id)
    if not ticket:
        logging.error("Error en Ejecución: No se pudo reservar")
        raise HTTPException(status_code=400, detail="Unable to reserve ticket")
    logging.info("Éxito en Ejecución: Ticket reservado")
    return {"message": "Ticket reserved successfully"}

@app.post("/tickets/{ticket_id}/buy")
async def buy_ticket_endpoint(ticket_id: int, user_id: int, db: AsyncSession = Depends(get_db)):
    ticket = await buy_ticket(db, ticket_id, user_id)
    if not ticket:
        logging.error("Error en Ejecución: No se pudo comprar")
        raise HTTPException(status_code=400, detail="Unable to buy ticket")
    logging.info("Éxito en Ejecución: Ticket comprado")
    return {"message": "Ticket purchased successfully"}

@app.post("/tickets/{ticket_id}/cancel")
async def cancel_ticket_endpoint(ticket_id: int, db: AsyncSession = Depends(get_db)):
    ticket = await cancel_reservation(db, ticket_id)
    if not ticket:
        logging.error("Error en Ejecución: No se pudo cancelar")
        raise HTTPException(status_code=400, detail="Unable to cancel ticket")
    logging.info("Éxito en Ejecución: Reserva cancelada")
    return {"message": "Ticket reservation canceled"}