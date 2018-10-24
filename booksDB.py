import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

df = pd.read_json('books.json')
print(df.columns)

class Book(Base):
    
    __tablename__ = 'book'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    subtitle = Column(String(250))
    description = Column(String(250))
    isbn = Column(String(250))
    publishers = Column(String(250))
    yearID = Column(Integer, ForeignKey('year.id'))
    authorID = Column(Integer, ForeignKey('author.id'))
    
class Author(Base):
    
    __tablename__ = 'author'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False)
       
    
class Year(Base):
    
    __tablename__ = 'year'
    
    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    

engine = create_engine('sqlite:///books.db')
Base.metadata.create_all(engine)