from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from crud.users import (
    get_user_by_email,
    create_user,
    get_users,
    get_user_by_id
)
import schemas

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post(
    "/",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user_endpoint(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    return create_user(db=db, user=user)

@router.get(
    "/",
    response_model=list[schemas.UserResponse]
)
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return get_users(db, skip=skip, limit=limit)

@router.get(
    "/{user_id}",
    response_model=schemas.UserResponse
)
def read_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    db_user = get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return db_user
