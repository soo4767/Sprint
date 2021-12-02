import database
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from repository import team as team_repository
from schemas import team as team_schema

router = APIRouter(
    prefix="/team",
    tags=['team']
)

get_db = database.get_db


@router.post('', response_model=team_schema.Team)
def create(request: team_schema.CreateTeam, db: Session = Depends(get_db)):
    return team_repository.create(request, db)


@router.put('')
def update(request: team_schema.UpdateTeam, db: Session = Depends(get_db)):
    return team_repository.update(request, db)


@router.put('/invite')
def invite_user(request: team_schema.InviteUserToTeam, db: Session = Depends(get_db)):
    return team_repository.invite(request, db)


@router.get('/{team_id}')
def get(team_id: int, db: Session = Depends(get_db)):
    return team_repository.get(team_id, db)


@router.delete('/{team_id}')
def delete(team_id: int, db: Session = Depends(get_db)):
    return team_repository.delete(team_id, db)


@router.get('/{team_id}/user-list')
def get_user_list_by_team(team_id: int, db: Session = Depends(get_db)):
    return team_repository.get_user_list_by_team(team_id, db)
