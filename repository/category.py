from sqlalchemy.orm import Session
from models import category as category_model
from repository import team as team_repository
from schemas import category as category_schema
from fastapi import status, HTTPException


def get(category_id: int, db: Session):
    category = db.query(category_model.Category).filter(category_model.Category.category_id == category_id).first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found category with id {category_id}")

    return category


def get_by_name(category_name: str, db: Session):
    category = db.query(category_model.Category).filter(category_model.Category.category_name == category_name).first()
    return category


def create(request: category_schema.CreateCategory, db: Session):
    category = get_by_name(request.category_name, db)

    if category:
        category.team_list.append(team_repository.get(request.team_id, db))
        db.commit()
        db.refresh(category)
        return category

    category = category_model.Category()
    category.category_name = request.category_name

    category.team_list.append(team_repository.get(request.team_id, db))

    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def update(request: category_schema.UpdateCategory, db: Session):
    category = get_by_name(request.category_name, db)

    if category:
        return category

    category = get(request.category_id, db)

    if len(category.team_list) == 1:
        category.category_name = request.category_name
        db.commit()
        db.refresh(category)
        return category
    else:
        req = category_schema.CreateCategory()
        req.category_name = request.category_name
        req.team_id = request.team_id
        return create(req, db)


def delete(request: category_schema.DeleteCategory, db: Session):
    category = get(request.category_id, db)

    if len(category.team_list) == 1:
        db.delete(category)
        db.commit()
    else:
        category.team_list.remove(team_repository.get(request.team_id, db))
        db.commit()
        db.refresh(category)

    return "Delete Category Success"
