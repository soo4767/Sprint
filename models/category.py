from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import team_category, board_category


class Category(Base):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String)

    category_value = relationship(
        'Board',
        secondary='board_category_relation',
        # primaryjoin="models.category.Category.category_id == models.board_category.BoardCategoryRelation.category_id",
        # secondaryjoin=" models.board_category.BoardCategoryRelation.board_id == models.board.Board.board_id",
    )

    team_list = relationship("Team", secondary=team_category.team_category_relation, back_populates='category_list')
