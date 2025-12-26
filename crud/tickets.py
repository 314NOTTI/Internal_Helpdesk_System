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

