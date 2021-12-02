import database
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/comment",
    tags=['Comment']
)

get_db = database.get_db


@router.post('')
def create(db: Session = Depends(get_db)):
    return 'aaa'


@router.get('/{comment_id}')
def get(db: Session = Depends(get_db)):
    return 'aaa'


@router.put('/{comment_id}')
def update(db: Session = Depends(get_db)):
    return 'aaa'


@router.delete('/{comment_id}')
def delete(db: Session = Depends(get_db)):
    return 'aaa'


@router.get('/list/board/{board_id}')
def get(db: Session = Depends(get_db)):
    return 'aaa'


@router.get('/list/user/{user_id}')
def get(db: Session = Depends(get_db)):
    return 'aaa'
