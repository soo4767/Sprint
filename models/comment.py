from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Comment(Base):
    __tablename__ = 'comment'

    comment_id = Column(Integer, primary_key=True)
    comment_content = Column(String)

    user_id = Column(Integer, ForeignKey('user.user_id', ondelete="SET NULL"))
    board_id = Column(Integer, ForeignKey('board.board_id', ondelete="CASCADE"))
