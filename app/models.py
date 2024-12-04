from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String, index=True)
    customer_name = Column(String)
    status = Column(String)  # reserved, purchased, canceled
    created_at = Column(DateTime)