from sqlalchemy import Column, Integer, Table, ForeignKey
from database import Base

team_category_relation = Table('team_category_relation', Base.metadata,
                               Column('category_id', Integer, ForeignKey('category.category_id', ondelete="CASCADE")),
                               Column('team_id', Integer, ForeignKey('team.team_id', ondelete="CASCADE"))
                               )
