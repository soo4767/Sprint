from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .user_team import user_team_relation


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    password = Column(String)

    board_list = relationship("Board")
    comment_list = relationship("Comment")
    team_list = relationship("Team", secondary=user_team_relation, back_populates='user_list')
