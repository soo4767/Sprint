from sqlalchemy import Column, Integer, Table, ForeignKey
from database import Base

board_layer = Table('board_layer', Base.metadata,
                    Column('child_id', Integer, ForeignKey('board.board_id', ondelete="CASCADE")),
                    Column('parent_id', Integer, ForeignKey('board.board_id', ondelete="CASCADE"))
                    )
