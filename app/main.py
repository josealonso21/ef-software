from fastapi import FastAPI
from app.routers import tickets
from app.database import engine, Base

init_database()

app = FastAPI()
app.include_router(tickets.router)
