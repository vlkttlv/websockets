from app.database import Base
from sqlalchemy import Column, Computed, Date, Integer, ForeignKey, String, Text
from sqlalchemy.orm import relationship


class Message(Base):

    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey("users.id"))  # отправитель
    recipient_id = Column(Integer, ForeignKey("users.id"))  # получатель
    content = Column(Text, nullable=False)
