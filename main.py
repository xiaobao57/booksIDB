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

#@app.route('/bookhome/')
@app.route('/bookhome/<int:bookid>')
def bookinfo(bookid):
 
    book = db.session.query(Book).filter(Book.id == bookid).first()
    #authorID = db.session.query(authorlist).filter(authorlist.bookID == bookid).first()
    #author = db.session.query(Author).filter(Author.id == authorID).first()
    return render_template('book.html', book = book) #, author = author)

@app.route('/authorhome/<int:authorid>')
def authorinfo(authorid):
 
    authorBook = db.session.query(authorlist).filter(authorlist.bookID == authorid).first()
    author = db.session.query(Author).filter(Author.id == authorBook.authorID).first()

    return render_template('author.html', author = author)

@app.route('/publisherhome/<int:publisherid>')
def publisherinfo(publisherid):

    publisher = db.session.query(Publisher).filter(Publisher.id == publisherid).first()
    return render_template('publisher.html', publisher = publisher)
 

if __name__ == "__main__":
 app.run()
#----------------------------------------
# end of main.py
#----------------------------------------
