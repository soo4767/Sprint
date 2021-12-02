from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    user_name: str
    password: str


class UpdateUser(BaseModel):
    user_id: int
    user_name: Optional[str]
    password: Optional[str]


class UserNamePassword(BaseModel):
    user_name: str
    password: str


class UserIdName(BaseModel):
    user_id: int
    user_name: str

    class Config:
        orm_mode = True
