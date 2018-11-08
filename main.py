#-----------------------------------------
# main.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template

from booksDB import app, db, Book, Author, Publisher

from loadDB import loadBooks

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@app.route('/')
def index():
 books = db.session.query(Book).all()

 return render_template('hello.html', books = books)

@app.route('/')
def bookHome():
 return render_template('hello.html', value=0)

@app.route('/')
def authorHome():
 return render_template('hello.html',  value=1)

@app.route('/')
def publisherHome():
 return render_template('hello.html',  value=2)

@app.route('/about')
def about():
 return render_template('about.html')

#----------------------------------------
# Model Pages
#----------------------------------------

@app.route('/book')
def book():
 return render_template('book.html')

@app.route('/author')
def author():
 return render_template('author.html')

@app.route('/publisher')
def publisher():
 return render_template('publisher.html')

###Need to delete
#----------------------------------------
# Test Nav
#----------------------------------------

@app.route('/navtest')
def navtest():
 return render_template('navtest.html')
 
#----------------------------------------
# Books
#----------------------------------------

@app.route('/sorcerors-stone/')
def sorcerors_stone():
 return render_template('sorcerors-stone.html')

@app.route('/mistborn/')
def mistborn():
 return render_template('mistborn.html')

@app.route('/all-the-pres-men/')
def all_the_pres_men():
 return render_template('all-the-pres-men.html')


#----------------------------------------
# Authors
#----------------------------------------

@app.route('/jk-rowling/')
def jk_rowling():
 return render_template('jk-rowling.html')

@app.route('/brandon-sanderson/')
def brandon_sanderson():
 return render_template('brandon-sanderson.html')

@app.route('/carl-bernstein/')
def carl_bernstein():
 return render_template('carl-bernstein.html')

#----------------------------------------
# Publishers
#----------------------------------------

@app.route('/pottermore/')
def pottermore():
 return render_template('pottermore.html')

@app.route('/simon-schuster/')
def simon_schuster():
 return render_template('simon-schuster.html')

@app.route('/palgrave-mac/')
def palgrave_mac():
 return render_template('palgrave-mac.html')

if __name__ == "__main__":
 app.run()
#----------------------------------------
# end of main.py
#----------------------------------------
