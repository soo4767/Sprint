import database
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from repository import user
from schemas import user as user_schema

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=user_schema.ShowUser)
def create_user(request: user_schema.User, db: Session = Depends(get_db)):
    return user.create(request, db)
