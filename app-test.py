from app import app

import unittest


class BasicTestCase(unittest.TestCase):

	def test_get_all_books(self):
		"""Tests if GET /books returns all books"""
		tester = app.test_client(self)
		response = tester.get('/books', content_type="html/text")
		self.assertEqual(response.status_code, 200)

	def test_post_book(self):
		"""Test POST /books"""
		tester = app.test_client(self)
		response = tester.post('/books', content_type="application/json")
		self.assertEqual(response.status_code, 200)






if __name__ == '__main__':
	unittest.main()
