from sqlalchemy import Column, Integer, Table, ForeignKey, String
from database import Base

board_category_relation = Table('board_category_relation', Base.metadata,
                                Column('category_id', Integer, ForeignKey('category.category_id', ondelete="CASCADE")),
                                Column('board_id', Integer, ForeignKey('board.board_id', ondelete="CASCADE")),
                                Column('value', String)
                                )
