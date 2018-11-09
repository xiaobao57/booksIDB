#-----------------------------------------
# main.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template
from models import app, db, Book, Author, Publisher, authorlist
from loadDB import loadBooks
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import subprocess


@app.route('/')
def index():
    books = db.session.query(Book).all()

    return render_template('hello.html', books = books)

@app.route('/about')
def about():
	p = subprocess.Popen(["python", "test.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	out, err = p.communicate()
	output=err+out
	output = output.decode("utf-8") #convert from byte type to string type
	return render_template('about.html', output = "<br/>".join(output.split("\n")))

#----------------------------------------
# Model Pages
#----------------------------------------

@app.route('/bookhome/<int:pagenum>')
def bookhome(pagenum):
    books = db.session.query(Book).all()
    print(books)
    if pagenum < 11:
        booksToPass = books[:pagenum]
    else:
        booksToPass = books[pagenum - 10:pagenum]

    booksCount = books = len(db.session.query(Book).all()) // 10

    return render_template('bookhome.html', books = booksToPass, booksCount = booksCount)

@app.route('/authorhome/<int:pagenum>')
def authorhome(pagenum):
    authors = db.session.query(Author).all()
    if pagenum < 11:
        authorsToPass = authors[:pagenum]
    else:
        authorsToPass = authors[pagenum - 10:pagenum]

    authorsCount = len(authors) // 10
    return render_template('authorhome.html', authors = authorsToPass, authorsCount = authorsCount)

@app.route('/publisherhome/<int:pagenum>')
def publisherhome(pagenum):
    publishers = db.session.query(Publisher).all()
    if pagenum < 11:
        pubToPass = publishers[:pagenum]
    else:
        pubToPass = publishers[pagenum - 10:pagenum]

    pubCount = len(publishers) // 10
    return render_template('publisherhome.html', publishers = pubToPass, pubCount = pubCount )

#----------------------------------------
# Books, Authors, Publishers
#----------------------------------------

#@app.route('/bookhome/')
@app.route('/book/<int:passedid><string:page>')
def bookinfo(passedid, page):
 
    if(page == "book"):
        book = db.session.query(Book).filter(Book.id == passedid).first()
    elif(page == "author"):
        authorBook = db.session.query(authorlist).filter(authorlist.bookID == passedid).first()
        book = db.session.query(Book).filter(Book.id == authorBook.bookID).first()
    else: 
        book = db.session.query(Book).filter(Book.id == passedid).first()
    #authorID = db.session.query(authorlist).filter(authorlist.bookID == bookid).first()
    #author = db.session.query(Author).filter(Author.id == authorID).first()
    return render_template('book.html', book = book) #, author = author)

@app.route('/author/<int:passedid><string:page>')
def authorinfo(passedid, page):
 
    if(page == "book"):
        authorBook = db.session.query(authorlist).filter(authorlist.bookID == passedid).first()
        author = db.session.query(Author).filter(Author.id == authorBook.authorID).first()
    elif(page == "author"):
        author = db.session.query(Author).filter(Author.id == passedid).first()
    else:
        authorBook = db.session.query(authorlist).filter(authorlist.bookID == passedid).first()
        book = db.session.query(Book).filter(Book.id == authorBook.bookID).first()
        author = db.session.query(Author).filter(Author.id == book.id).first()

    return render_template('author.html', author = author)

@app.route('/publisher/<int:passedid><string:page>')
def publisherinfo(passedid, page):

    if(page == 'book'):
        publisher = db.session.query(Publisher).filter(Publisher.id == passedid).first()
    elif(page=='author'):
        authorBook = db.session.query(authorlist).filter(authorlist.bookID == passedid).first()
        book = db.session.query(Book).filter(Book.id == authorBook.bookID).first()
        publisher = db.session.query(Publisher).filter(Publisher.id == book.id).first()
    else:
        publisher = db.session.query(Publisher).filter(Publisher.id == passedid).first()

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
