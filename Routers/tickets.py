from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import SessionLocal
from crud.tickets import create_ticket
import schemas

router = APIRouter(
    prefix="/tickets",
    tags=["tickets"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post(
    "/",
    response_model=schemas.TicketResponse,
    status_code=status.HTTP_201_CREATED
)
def create_ticket_endpoint(
    ticket: schemas.TicketCreate,
    db: Session = Depends(get_db)
):
    return create_ticket(db=db, ticket=ticket)
