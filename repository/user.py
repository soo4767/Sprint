from sqlalchemy.orm import Session
from models import user as user_model
from schemas import user as user_schema
from fastapi import status, HTTPException


def create(request: user_schema.UserNamePassword, db: Session):
    new_user = user_model.User(user_name=request.user_name, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get(user_id: int, db: Session):
    user = db.query(user_model.User).filter(user_model.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not found user with id {user_id}")
    return user


def get_user_list(db: Session, page, page_size):
    user_list = db.query(user_model.User)
    if page_size:
        user_list = user_list.limit(page_size)
    if page:
        user_list = user_list.offset(page * page_size)
    return user_list.all()


def delete(user_id: int, db: Session):
    user = get(user_id, db)
    db.delete(user)
    db.commit()
    return f'Delete success user with id {user_id}'


def update(request: user_schema.UpdateUser, db: Session):
    user = get(request.user_id, db)

    if request.user_name:
        user.user_name = request.user_name

    if request.password:
        user.password = request.password

    db.commit()
    db.refresh(user)
    return user


def get_team_list_by_user(user_id: int, db: Session):
    user = get(user_id, db)
    return user.team_list
