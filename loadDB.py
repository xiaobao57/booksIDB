from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from booksDB import db, Book, Author, Publisher, authorList
import pandas as pd

''' sqlalchemy code
engine = create_engine('sqlite:///books.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
'''

df = pd.read_json('books.json')

def loadBooks():
    #author_id=1
    #publisher_id=1
    book_id = 1
    #authorList_id = 1
        
    for i in range(len(df)):
        
        book_id = book_id
        book_title = df['title'][i]
        book_description = df['description'][i]
        book_isbn = df['isbn'][i]
        book_publisher_date = df['publication_date'][i]
        book_google_id = df['google_id'][i]
        book_image_url = df['image_url'][i]
        book_publisherID = publisher_id
        book_authorListID = authorList_id
        book_id+=1
        
        newBook = Book(id=book_id, title=book_title, description=book_description, isbn=book_isbn, publisher_date=book_publisher_date,
                       goole_id=books_google_id,image_url=book_image_url, publisher=book_publisherID, authorList=book_authorList)
        
        db.session.add(newBook)
        db.session.commit()
        
        
        
        
        
        
        
        
        
        
        
        
        '''
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
        author_authorListID = authorList_id
        
        
        
        #query here, if publisher already exists, dont add info, else increase ID and add
        publisher_id = publisher_id
        publisher_name = df['publishers'][i][0]['name']
        try:
            publisher_wiki_url = df['publishers'][i][0]['wikipedia_url'] #nullable
        except:
            publisher_wiki_url = None
        try:
            publisher_parent_company = df['publishers'][i][0]['parent_company'] #nullable
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
        
        authorList_id = authorList_id
        authorList_bookID = book_id
        authorList_authorID = author_id
        
        book_id+=1
        authorList_id+=1
        '''

load()