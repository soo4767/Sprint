import database
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from schemas import category as category_schema
from repository import category as category_repository

router = APIRouter(
    prefix="/category",
    tags=['Category']
)

get_db = database.get_db


@router.post('')
def create(request: category_schema.CreateCategory, db: Session = Depends(get_db)):
    return category_repository.create(request, db)


@router.put('')
def update(request: category_schema.UpdateCategory, db: Session = Depends(get_db)):
    return category_repository.update(request, db)


@router.delete('')
def delete(request: category_schema.DeleteCategory, db: Session = Depends(get_db)):
    return category_repository.delete(request, db)


@router.get('/{category_id}')
def get(category_id: int, db: Session = Depends(get_db)):
    return category_repository.get(category_id, db)
