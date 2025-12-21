from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine 
from models import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown (se precisar no futuro) 

app = FastAPI(
    title="Internal Helpdesk System",
    lifespan=lifespan
)

@app.get("/")
def root():
    return {"status": "ok", "message": "Internal Helpdesk System is running"}