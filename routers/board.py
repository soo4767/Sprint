import database
from typing import Optional, List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from schemas import board as board_schema
from repository import board as board_repository

router = APIRouter(
    prefix="/board",
    tags=['Board']
)

get_db = database.get_db


@router.post('', response_model=board_schema.Board)
def create(request: board_schema.CreateBoard, db: Session = Depends(get_db)):
    return board_repository.create(request, db)


@router.put('', response_model=board_schema.BoardDetail)
def update(request: board_schema.UpdateBoard, db: Session = Depends(get_db)):
    return board_repository.update(request, db)


@router.get('/{board_id}', response_model=board_schema.BoardDetail)
def get(board_id: int, db: Session = Depends(get_db)):
    return board_repository.get(board_id, db)


@router.delete('/{board_id}')
def delete(board_id: int, db: Session = Depends(get_db)):
    return board_repository.delete(board_id, db)


@router.get('/list/team/{team_id}', response_model=List[board_schema.BoardDetail])
def get_board_list_by_team(team_id: int, db: Session = Depends(get_db)):
    return board_repository.get_board_list_by_team(team_id, db)


@router.get('/list/user/{user_id}', response_model=List[board_schema.BoardDetail])
def get_board_list_by_user(user_id: int, db: Session = Depends(get_db)):
    return board_repository.get_board_list_by_user(user_id, db)
