from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .user_team import user_team_relation
from .team_category import team_category_relation


class Team(Base):
    __tablename__ = 'team'

    team_id = Column(Integer, primary_key=True)
    team_name = Column(String)

    board_list = relationship("Board", back_populates='team')
    user_list = relationship("User", secondary=user_team_relation, back_populates='team_list')
    category_list = relationship('Category', secondary=team_category_relation)
