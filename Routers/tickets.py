from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from crud.tickets import create_ticket, get_tickets, get_ticket_by_id
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

@router.get(
    "/",
    response_model=list[schemas.TicketResponse]
)
def read_tickets(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return get_tickets(db, skip=skip, limit=limit)

@router.get(
    "/{ticket_id}",
    response_model=schemas.TicketResponse
)
def read_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):
    ticket = get_ticket_by_id(db, ticket_id=ticket_id)
    if ticket is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )
    return ticket

