from app.database import Base
from sqlalchemy import Column, Computed, Date, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class Message(Base):

    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    