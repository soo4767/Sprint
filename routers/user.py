import database
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from repository import user as user_repository
from schemas import user as user_schema

router = APIRouter(
    prefix="/user",
    tags=['User']
)

get_db = database.get_db


@router.post('', response_model=user_schema.UserIdName)
def create(request: user_schema.UserNamePassword, db: Session = Depends(get_db)):
    return user_repository.create(request, db)


@router.put('')
def update(request: user_schema.UpdateUser, db: Session = Depends(get_db)):
    return user_repository.update(request, db)


@router.get('/list')
def get_user_list(db: Session = Depends(get_db), page: Optional[int] = 0, page_size: Optional[int] = None):
    return user_repository.get_user_list(db, page, page_size)


@router.get('/{user_id}', response_model=user_schema.UserIdName)
def get(user_id: int, db: Session = Depends(get_db)):
    return user_repository.get(user_id, db)


@router.delete('/{user_id}')
def delete(user_id: int, db: Session = Depends(get_db)):
    return user_repository.delete(user_id, db)


@router.get('/{user_id}/team-list')
def get_team_list_by_user(user_id: int, db: Session = Depends(get_db)):
    return user_repository.get_team_list_by_user(user_id, db)
