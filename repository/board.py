from sqlalchemy.orm import Session
from models import board as board_model
from models import board_category as board_category_model
from repository import user as user_repository
from repository import team as team_repository
from repository import category as category_repository
from schemas import board as board_schema
from fastapi import status, HTTPException


def create(request: board_schema.CreateBoard, db: Session):
    new_board = board_model.Board()
    new_board.board_content = request.board_content
    new_board.board_status = request.board_status

    new_board.team_id = team_repository.get(request.team_id, db).team_id
    new_board.user_id = user_repository.get(request.user_id, db).user_id

    if request.parent_id:
        new_board.parent_id = get(request.parent_id, db).board_id

    db.add(new_board)
    db.commit()
    db.refresh(new_board)
    return new_board


def get(board_id: int, db: Session):
    board = db.query(board_model.Board).filter(board_model.Board.board_id == board_id).first()
    if not board:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not found user with id {board_id}")

    return board


def update(request: board_schema.UpdateBoard, db: Session):
    board = get(request.board_id, db)

    if request.parent_id:
        board.parent_id = request.parent_id

    if request.board_status:
        board.board_status = request.board_status

    if request.board_content:
        board.board_content = request.board_content

    if request.category_list:
        for category in request.category_list:
            category_repository.get(category.category_id, db)
            # test = board_category_model.board_category_relation.select().where(
            #     board_category_model.board_category_relation.c.category_id == category.category_id)
            # # test = db.query(board_category_model.board_category_relation).filter()
            # test2 = db.execute(test)
            # print('test')
            test = db.query(board_category_model.BoardCategoryRelation).filter(
                board_category_model.BoardCategoryRelation.category_id == category.category_id).all()
            print('test')
        pass
    db.commit()
    return board


def delete(board_id: int, db: Session):
    board = get(board_id, db)
    db.delete(board)
    db.commit()
    return f'Delete Success Board with id {board_id}'


def get_board_list_by_team(team_id: int, db: Session):
    team = team_repository.get(team_id, db)

    return db.query(board_model.Board).filter(board_model.Board.team_id == team.team_id).all()


def get_board_list_by_user(user_id: int, db: Session):
    user = user_repository.get(user_id, db)
    return db.query(board_model.Board).filter(board_model.Board.user_id == user.user_id).all()
