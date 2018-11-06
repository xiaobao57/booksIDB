import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Book(Base):
    
    __tablename__ = 'book'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(250))
    isbn = Column(String(250))
    publisher_date = Column(String(250))
    google_id = Column(Integer)
    image_url = Column(String(250))
    publisherID = Column(Integer, ForeignKey('publisher.id'))
    authorListID = Column(Integer, ForeignKey('authorList.id'))
    
class Author(Base):
    
    __tablename__ = 'author'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False)
    born = Column(Integer)
    education = Column(String(250))
    nationality = Column(String(250))
    alma_mater = Column(String(250))
    wiki_url = Column(String(250))
    image_url = Column(String(250))
    authorListID = Column(Integer, ForeignKey('authorList.id'))
       
    
class Publisher(Base):
    
    __tablename__ = 'publisher'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    wiki_url = Column(String(250))
    parent_company = Column(String(250))
    founded = Column(Integer)
    description = Column(String(250))
    image_url = Column(String(250))
    website = Column(String(250))

class authorList(Base):

    __tablename__ = 'authorList'

    id = Column(Integer, primary_key=True)
    bookID = Column(Integer, ForeignKey('book.id'))
    author = Column(Integer, ForeignKey('author.id'))


engine = create_engine('sqlite:///books.db')
Base.metadata.create_all(engine)