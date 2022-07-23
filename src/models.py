import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    


class Followers(Base):
    __tablename__ = "follower"
    id = Column(Integer, primary_key=True)
    user_from = relationship(User)
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    user_to = relationship(User)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=True)

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    type_of = Column(Enum)
    url = Column(String)
    post = relationship(Post)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=True)


class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String)
    author = relationship(User)
    author_id = Column(Integer, ForeignKey('author.id'), nullable=True)
    post = relationship(Post)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=True)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')