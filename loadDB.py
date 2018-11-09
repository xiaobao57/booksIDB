from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from booksDB import db, Book, Author, Publisher, authorlist
import pandas as pd

''' sqlalchemy code
engine = create_engine('sqlite:///books.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
'''

df = pd.read_json('books.json')

publisher_id=1
book_id = 1
authorList_id = 1

def loadBooks():
    publisher_id=1
    book_id = 1
    authorList_id = 1

    for i in range(len(df)):
        
        book_id = book_id
        book_title = df['title'][i]
        book_description = df['description'][i]
        book_isbn = df['isbn'][i]
        book_publisher_date = df['publication_date'][i]
        book_google_id = df['google_id'][i]
        book_image_url = df['image_url'][i]
        book_publisherID = publisher_id
        
        publishers = db.session.query(Publisher).all()
        for publisher in publishers:
            if df['publishers'][i][0]['name'] == publisher.name:
                book_publisherID = publisher.id
                #print(book_publisherID)

        newBook = Book(id=book_id, title=book_title, description=book_description, isbn=book_isbn, publisher_date=book_publisher_date,
                       google_id=book_google_id,image_url=book_image_url, publisherID=book_publisherID)
        
        db.session.add(newBook)
        db.session.commit()

        book_id+=1

def loadAuthors():
    author_id = 1

    for i in range(len(df)):
        author_id = author_id
        try:
            author_born = df['authors'][i][0]['born'] #nullable
        except:
            author_born = None
        try:
            author_name = df['authors'][i][0]['name']
        except:
            author_name = None
        try:
            author_education = df['authors'][i][0]['education'] #nullable
        except:
            author_education = None
        try:
            author_nationality = df['authors'][i][0]['nationality'] #nullable
        except:
            author_nationality = None
        try:
            author_description = df['authors'][i][0]['description'] #nullable
        except:
            author_description = None
        try:
            author_alma_mater = df['authors'][i][0]['alma_mater'] #nullable
        except:
            author_alma_mater = None
        try:
            author_wiki_url = df['authors'][i][0]['wikipedia_url'] #nullable
        except:
            author_wiki_url = None
        try:
            author_image_url = df['authors'][i][0]['image_url'] #nullable
        except:
            author_image_url = None

        authors = db.session.query(Author).all()
        aList = []
        for author in authors:
            aList.append(author.name)
            
        if author_name not in aList:
            newAuth = Author(id=author_id, name=author_name, born=author_born, nationality=author_nationality,
                education=author_education, alma_mater=author_alma_mater, wiki_url=author_wiki_url,
                image_url=author_image_url)
            db.session.add(newAuth)
            db.session.commit()
            author_id += 1

def loadPublishers():
    publisher_id = 1

    for i in range(len(df)):
        publisher_id = publisher_id
        publisher_name = df['publishers'][i][0]['name']
        try:
            publisher_wiki_url = df['publishers'][i][0]['wikipedia_url'] #nullable
        except:
            publisher_wiki_url = None
        try:
            publisher_parent_company = df['publishers'][i][0]['parent company'] #nullable
        except:
            publisher_parent_company = None
        try:
            publisher_founded = df['publishers'][i][0]['founded'] #nullable
        except:
            publisher_founded = None
        try:
            publisher_description = df['publishers'][i][0]['description'] #nullable
        except:
            publisher_description = None
        try:
            publisher_owner = df['publishers'][i][0]['owner'] #nullable
        except:
            publisher_owner = None
        try:
            publisher_image_url = df['publishers'][i][0]['image_url'] #nullable
        except:
            publisher_image_url = None
        try:
            publisher_website = df['publishers'][i][0]['website'] #nullable
        except:
            publisher_website = None

        publishers = db.session.query(Publisher).all()
        pList = []
        for publisher in publishers:
            pList.append(publisher.name)
            
        if publisher_name not in pList:
            newPub = Publisher(id=publisher_id,name=publisher_name,wiki_url=publisher_wiki_url,
                parent_company=publisher_parent_company,founded=publisher_founded,description=publisher_description,
                image_url=publisher_image_url,website=publisher_website)
            db.session.add(newPub)
            db.session.commit()
            publisher_id += 1

def loadAuthorList():
    authorListID = 1

    for i in range(len(df)):

        authors = db.session.query(Author).all()
        for author in authors:
            if df['authors'][i][0]['name'] == author.name:
                author_ID = author.id

        books = db.session.query(Book).all()
        for book in books:
            if df['title'][i] == book.title:
                book_ID = book.id

        newAuthList = authorlist(id=authorListID, bookID=book_ID, authorID=author_ID)
        db.session.add(newAuthList)
        db.session.commit()
        authorListID += 1

# loadPublishers()
# loadBooks()
# loadAuthors()
# loadAuthorList()
