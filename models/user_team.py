from sqlalchemy import Column, Integer, Table, ForeignKey
from database import Base

user_team_relation = Table('user_team_relation', Base.metadata,
                           Column('user_id', Integer, ForeignKey('user.user_id', ondelete="CASCADE")),
                           Column('team_id', Integer, ForeignKey('team.team_id', ondelete="CASCADE"))
                           )
