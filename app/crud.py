from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import Ticket

async def get_ticket_by_id(db: AsyncSession, ticket_id: int):
    result = await db.execute(select(Ticket).where(Ticket.id == ticket_id))
    return result.scalar_one_or_none()

async def update_ticket_status(db: AsyncSession, ticket_id: int, status: str, user_id=None):
    ticket = await get_ticket_by_id(db, ticket_id)
    if ticket:
        ticket.status = status
        ticket.user_id = user_id
        await db.commit()
        await db.refresh(ticket)
    return ticket