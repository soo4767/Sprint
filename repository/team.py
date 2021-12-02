from sqlalchemy.orm import Session
from models import team as team_model
from repository import user as user_repository
from schemas import team as team_schema
from fastapi import status, HTTPException


def create(request: team_schema.CreateTeam, db: Session):
    new_team = team_model.Team(team_name=request.team_name)
    new_team.user_list.append(user_repository.get(request.user_id, db))
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return new_team


def invite(request: team_schema.InviteUserToTeam, db: Session):
    team = get(request.team_id, db)
    for user_id in request.user_id_list:
        user = user_repository.get(user_id, db)
        if user not in team.user_list:
            team.user_list.append(user)
    db.commit()


def get(team_id: int, db: Session):
    team = db.query(team_model.Team).filter(team_model.Team.team_id == team_id).first()
    if not team:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not found team with id {team_id}")
    return team


def update(request: team_schema.UpdateTeam, db: Session):
    team = get(request.team_id, db)

    if request.team_name:
        team.team_name = request.team_name
        
    db.commit()
    db.refresh(team)
    return team


def delete(team_id: int, db: Session):
    team = get(team_id, db)
    db.delete(team)
    db.commit()
    return f'Delete success team with id {team_id}'


def get_user_list_by_team(team_id: int, db: Session):
    team = get(team_id, db)
    return team.user_list
