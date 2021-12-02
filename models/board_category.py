from sqlalchemy import Column, Integer, ForeignKey, String
from database import Base
from sqlalchemy.orm import relationship


class BoardCategoryRelation(Base):
    __tablename__ = 'board_category_relation'

    # id = Column(Integer, primary_key=True)
    category_id = Column(ForeignKey('category.category_id', ondelete="CASCADE"), primary_key=True)
    board_id = Column(ForeignKey('board.board_id', ondelete="CASCADE"), primary_key=True)
    value = Column(String)

    board = relationship('Board', backref="board_relation")
    category = relationship('Category', backref="category_relation")
