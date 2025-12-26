from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine
from models import Base
from routers import users, tickets

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title="Internal Helpdesk System",
    lifespan=lifespan
)

app.include_router(users.router)
app.include_router(tickets.router)

@app.get("/")
def root():
    return {"status": "ok", "message": "Internal Helpdesk System is running"}
