from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TicketBase(BaseModel):
    title: str
    description: str
    priority: int

class TicketCreate(TicketBase):
    pass

class ticketread(TicketBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True