#-----------------------------------------
# main.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template
from booksDB import app, db, Book, Author, Publisher, authorlist
from loadDB import loadBooks
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@app.route('/')
def index():
    books = db.session.query(Book).all()
    return render_template('hello.html', books = books)

@app.route('/about')
def about():
    return render_template('about.html')

#----------------------------------------
# Model Pages
#----------------------------------------

@app.route('/bookhome/<int:pagenum>')
def bookhome(pagenum):
    books = db.session.query(Book).all()
    if pagenum < 11:
        booksToPass = books[:pagenum]
    else:
        booksToPass = books[pagenum - 10:pagenum]

    booksCount = books = len(db.session.query(Book).all()) // 10
    # authors = db.session.query(Author).all()
    # publishers = db.session.query(Publisher).all()
    return render_template('bookhome.html', books = booksToPass, booksCount = booksCount)

@app.route('/authorhome')
def authorhome():
    authors = db.session.query(Author).all()
    return render_template('authorhome.html', authors = authors)

@app.route('/publisherhome')
def publisherhome():
    publishers = db.session.query(Publisher).all()
    return render_template('publisherhome.html', publishers = publishers)

#----------------------------------------
# Books, Authors, Publishers
#----------------------------------------

@app.route('/book/')
@app.route('/book/<int:bookid>')
def book(bookid):
    book = db.session.query(Book).filter(Book.id == bookid).first()
    #authorID = db.session.query(authorlist).filter(authorlist.bookID == bookid).first()
    #author = db.session.query(Author).filter(Author.id == authorID).first()
    return render_template('book.html', book = book) #, author = author)

# @app.route('/authorhome/<int:authorid>')
# def authorinfo(authorid):
 
#     book = db.session.query(Book).filter(Book.id == bookid).first()
#     authorID = db.session.query(authorlist).filter(authorlist.bookID == bookid).first()
#     author = db.session.query(Author).filter(Author.id == authorid).first()

#     return render_template('author.html', author = author)

@app.route('/publisherhome/<int:publisherid>')
def publisherinfo(publisherid):

    publisher = db.session.query(Publisher).filter(Publisher.id == publisherid).first()
    return render_template('publisher.html', publisher = publisher)


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
