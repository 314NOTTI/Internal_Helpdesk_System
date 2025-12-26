from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

class TicketBase(BaseModel):
    title: str
    description: str
    priority: int

class TicketCreate(TicketBase):
    pass

class TicketResponse(TicketBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True