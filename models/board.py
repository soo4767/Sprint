from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from models import board_category


class Board(Base):
    __tablename__ = 'board'

    board_id = Column(Integer, primary_key=True)
    board_content = Column(String)
    board_status = Column(String)

    team_id = Column(Integer, ForeignKey('team.team_id', ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey('user.user_id', ondelete="SET NULL"))

    parent_id = Column(Integer, ForeignKey('board.board_id'))
    parent = relationship('Board', remote_side="board.c.board_id", backref="child_list")

    category = relationship(
        "Category",
        secondary='board_category_relation',
        # primaryjoin="models.board.Board.board_id == models.board_category.BoardCategoryRelation.board_id",
        # secondaryjoin="models.board_category.BoardCategoryRelation.category_id == models.category.Category.category_id",
    )
