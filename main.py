#-----------------------------------------
# main.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template, request, redirect
from models import app, db, Book, Author, Publisher, authorlist
from loadDB import loadBooks
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import subprocess
from wtforms import Form, StringField, SelectField
from searchForm import SearchForm

@app.route('/', methods=['GET', 'POST'])
def index():
    books = db.session.query(Book).all()
    search = SearchForm(request.form)
    if request.method == 'POST':
            return search_results(search)
    return render_template('hello.html', form = search)

@app.route('/about')
def about():
	p = subprocess.Popen(["python", "test.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	out, err = p.communicate()
	output=err+out
	output = output.decode("utf-8") #convert from byte type to string type
	return render_template('about.html', output = "<br/>".join(output.split("\n")))

#----------------------------------------
# Search
#----------------------------------------
@app.route('/search')
def search_results(searchString):
    results = []

    print(searchString)
 
    return render_template('search.html', results = searchString.data['search'])



#----------------------------------------
# Model Pages
#----------------------------------------

@app.route('/bookhome/<int:pagenum>',  methods=['GET', 'POST'])
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
        book = db.session.query(Book).filter(Book.publisherID == passedid).first()
    return render_template('book.html', book = book)

@app.route('/author/<int:passedid><string:page>')
def authorinfo(passedid, page):
    
    if(page == "book"):
        authorBook = db.session.query(authorlist).filter(authorlist.bookID == passedid).first()
        author = db.session.query(Author).filter(Author.id == authorBook.authorID).first()
    elif(page == "author"):
        author = db.session.query(Author).filter(Author.id == passedid).first()
        books = db.session.query(Book).join(authorlist, authorlist.bookID == Book.id).\
            filter(authorlist.authorID == passedid).all()

        publishers = db.session.query(Publisher).join(Book, Book.publisherID == Publisher.id).\
            join(authorlist, authorlist.bookID == Book.id).\
            filter(Publisher.id == passedid).all()
    else:
        authorBook = db.session.query(authorlist).filter(authorlist.bookID == passedid).first()
        book = db.session.query(Book).filter(Book.id == authorBook.bookID).first()
        author = db.session.query(Author).filter(Author.id == book.id).first()

    return render_template('author.html', author = author, books = books , publishers = publishers)

@app.route('/publisher/<int:passedid><string:page>')
def publisherinfo(passedid, page):

    if(page == 'book'):
        publisher = db.session.query(Publisher).filter(Publisher.id == passedid).first()
    elif(page =='publisher'):
        authorBook = db.session.query(authorlist).filter(authorlist.bookID == passedid).first()
        book = db.session.query(Book).filter(Book.id == authorBook.bookID).first()
        publisher = db.session.query(Publisher).filter(Publisher.id == book.id).first()
        books = db.session.query(Book).filter(Book.publisherID == passedid).all()

        authors = db.session.query(Author).join(authorlist, authorlist.authorID == Author.id).\
            join(Book, Book.id == authorlist.bookID).\
            filter(Book.publisherID == passedid).all()
    else:
        publisher = db.session.query(Publisher).filter(Publisher.id == passedid).first()

    return render_template('publisher.html', publisher = publisher, books = books, authors = authors)
 


if __name__ == "__main__":
 app.run()
#----------------------------------------
# end of main.py
#----------------------------------------
