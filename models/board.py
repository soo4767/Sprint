from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .board_layer import board_layer


class Board(Base):
    __tablename__ = 'board'

    board_id = Column(Integer, primary_key=True)
    board_content = Column(String)
    board_status = Column(String)

    team_id = Column(Integer, ForeignKey('team.team_id', ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey('user.user_id', ondelete="SET NULL"))

    parent = relationship("Board", secondary=board_layer, back_populates='child_list', uselist=False)
    child_list = relationship("Board", secondary=board_layer, back_populates='parent')
