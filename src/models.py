import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)

    followers = relationship("Followers", backref='users', lazy=True)
    post = relationship("Post", backref='users', lazy=True)
    comment = relationship("Comment", backref='users', lazy=True)


class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {}


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    comment = relationship("Comment", backref='post', lazy=True)
    media = relationship("Media", backref='post', lazy=True)

    def to_dict(self):
        return {}


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    def to_dict(self):
        return {}


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum('Image', 'Video'), nullable=False)
    url = Column(String(100), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
