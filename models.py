from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    stories = relationship("Story", back_populates="owner")

class Story(Base):
    __tablename__ = "stories"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    description = Column(String)
    created_at = datetime.now()
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="stories")
    blocks = relationship("Block",back_populates="story")

class Block(Base):
     __tablename__ = "blocks"
     id = Column(Integer,primary_key=True,index=True)
     body = Column(String)
     created_at = datetime.now()
     story_id = Column(Integer,ForeignKey("stories.id"))
     story = relationship("Story",back_populates="blocks")
     