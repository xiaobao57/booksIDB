import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:[PASSWORD]@[IP ADDRESS]:[PORT]/[DB NAME]')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:hackstreetboys@35.202.39.27:5432/books')
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:rwbYRuby@localhost:5433/testbookdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):

    __tablename__ = 'book'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(9999))
    isbn = Column(String(250))
    publisher_date = Column(String(250))
    google_id = Column(String(250))
    image_url = Column(String(250))
    publisherID = Column(Integer)
    
class Author(db.Model):
    
    __tablename__ = 'author'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False)
    born = Column(String(250))
    education = Column(String(250))
    nationality = Column(String(250))
    alma_mater = Column(String(250))
    wiki_url = Column(String(250))
    image_url = Column(String(9999))
       
    
class Publisher(db.Model):
    
    __tablename__ = 'publisher'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(999), nullable=False)
    wiki_url = Column(String(999))
    parent_company = Column(String(999))
    founded = Column(String(999))
    description = Column(String(999))
    image_url = Column(String(999))
    website = Column(String(999))

class authorlist(db.Model):

    __tablename__ = 'authorlist'

    id = Column(Integer, primary_key=True)
    bookID = Column(Integer)
    authorID = Column(Integer)

db.drop_all()
db.create_all()