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

from typing import Optional

class TicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None
    status: Optional[str] = None
