from typing import List, Optional
from pydantic import BaseModel


class Category(BaseModel):
    category_id: int
    category_name: str

    class Config:
        orm_mode = True


class CreateCategory(BaseModel):
    team_id: int
    category_name: str


class UpdateCategory(BaseModel):
    team_id: int
    category_id: int
    category_name: str


class DeleteCategory(BaseModel):
    team_id: int
    category_id: int


class ShowCategoryWithValue(BaseModel):
    category_id: int
    category_name: str
    value: str

    class Config:
        orm_mode = True


class UpdateBoardCategory(BaseModel):
    category_id: int
    value: str
