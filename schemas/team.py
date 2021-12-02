from typing import List, Optional
from pydantic import BaseModel


class Team(BaseModel):
    team_id: int
    team_name: str

    class Config:
        orm_mode = True


class UpdateTeam(BaseModel):
    team_id: Optional[int]
    team_name: Optional[str]


class InviteUserToTeam(BaseModel):
    team_id: int
    user_id_list: List[int]


class CreateTeam(BaseModel):
    user_id: int
    team_name: str
