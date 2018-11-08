import os
import sys
import unittest
from models import db, Book

class DBTestCases(unittest.TestCase):
	def test_source_insert_1(self):
		r = db.session.query(Book).filter_by(id = '1').one()
		self.assertEqual(str(r.id), '1')

	def test_source_insert_2(self):
		r = db.session.query(Book).filter_by(id = '1').one()
		self.assertEqual(str(r.id), '1')

	def test_source_insert_3(self):
		r = db.session.query(Book).filter_by(id = '1').one()
		self.assertEqual(str(r.id), '1')
	
if __name__ == '__main__':
	unittest.main()