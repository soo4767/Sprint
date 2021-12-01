from sqlalchemy.orm import Session
from models import user as user_model
from schemas import user as user_schema


def create(request: user_schema.User, db: Session):
    new_user = user_model.User(user_name=request.user_name, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
