from database import Base
from sqlalchemy import Column, Integer, String


class Category(Base):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String)
