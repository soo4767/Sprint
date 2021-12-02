from typing import List, Optional
from pydantic import BaseModel

from schemas import category


class Board(BaseModel):
    board_id: int
    board_content: str
    board_status: str
    team_id: int
    user_id: int
    parent_id: Optional[int] = None

    class Config:
        orm_mode = True


class BoardDetail(BaseModel):
    board_id: int
    board_content: str
    board_status: str
    team_id: int
    user_id: int
    child_list: List[Board] = None
    parent: Board = None
    category_list: List[category.ShowCategoryWithValue] = None

    class Config:
        orm_mode = True


class CreateBoard(BaseModel):
    board_content: str
    board_status: str
    team_id: int
    user_id: int
    parent_id: Optional[int] = None


class UpdateBoard(BaseModel):
    board_id: int
    board_content: Optional[str]
    board_status: Optional[str]
    parent_id: Optional[int] = None
    category_list: List[category.UpdateBoardCategory] = None
