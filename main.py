from fastapi import FastAPI

from database import engine
from models import Base

app = FastAPI(title="Internal Helpdesk System")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"status": "ok", "message": "Internal Helpdesk System is running"}