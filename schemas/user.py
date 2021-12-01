from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    user_name: str
    password: str


class ShowUser(BaseModel):
    user_id: int
    user_name: str

    class Config:
        orm_mode = True
