import os
import sys
import unittest
from models import db, Book, Publisher, Author

class DBTestCases(unittest.TestCase):
	'''
	First 3 tests check if data exists in tables. Tests 4-6 check if the data in the table is correct.
	'''

	def test_source_insert_1(self):
		r = db.session.query(Book).filter_by(id = '1').one()
		self.assertEqual(str(r.id), '1')

	def test_source_insert_2(self):
		r = db.session.query(Author).filter_by(id = '1').one()
		self.assertEqual(str(r.id), '1')

	def test_source_insert_3(self):
		r = db.session.query(Publisher).filter_by(id = '1').one()
		self.assertEqual(str(r.id), '1')

	def test_source_insert_4(self):
		r = db.session.query(Book).filter_by(id = '1').one()
		self.assertEqual(str(r.title), "Harry Potter and the Sorcerer's Stone")

	def test_source_insert_5(self):
		r = db.session.query(Author).filter_by(id = '1').one()
		self.assertEqual(str(r.name), "J. K. Rowling")

	def test_source_insert_6(self):
		r = db.session.query(Publisher).filter_by(id = '1').one()
		self.assertEqual(str(r.name), "Pottermore")
	
if __name__ == '__main__':
	unittest.main()