from sqlalchemy.orm import Session
from models import Ticket
import schemas

def create_ticket(db: Session, ticket: schemas.TicketCreate):
    db_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        priority=ticket.priority
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def get_tickets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Ticket).offset(skip).limit(limit).all()

def get_ticket_by_id(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

def update_ticket(db: Session, ticket_id: int, ticket_data: schemas.TicketUpdate):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket is None:
        return None

    if ticket_data.title is not None:
        ticket.title = ticket_data.title
    if ticket_data.description is not None:
        ticket.description = ticket_data.description
    if ticket_data.priority is not None:
        ticket.priority = ticket_data.priority
    if ticket_data.status is not None:
        ticket.status = ticket_data.status

    db.commit()
    db.refresh(ticket)
    return ticket
