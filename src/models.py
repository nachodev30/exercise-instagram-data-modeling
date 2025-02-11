import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy import Enum

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    firstname = Column(String(250), nullable=False, unique=True)
    lastname = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)    
    posts = relationship('Post')
    comments = relationship('Comment')

class Followers(Base):
    __tablename__ = 'Followers'

    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id')) 
    followers = relationship(User)

class Comment(Base):
    __tablename__ = 'Comment'

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(1000), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post')


class Post(Base):
    __tablename__ = 'Post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Media(Base):
    __tablename__ = 'Media'

    id = Column(Integer, primary_key=True)
    type = Column(Enum('photo', 'reel', 'video'), unique=True)
    url = Column(String(250), unique=True)
    media_id = Column(Integer, ForeignKey('post.id'))
    media = relationship(Post)

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e