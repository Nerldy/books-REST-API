from app import app

import unittest


class HelloBooksAPITestCase(unittest.TestCase):
	"""Class represents Hello Books test cases"""

	def test_book_creation(self):
		"""Test POST /books will create a book"""
		pass

	def test_get_book(self):
		"""test GET /books returns all books in JSON format. If no books available it returns {"books": "None"}"""
		tester = app.test_client(self)
		response = tester.get('/books', content_type='application/json')
		self.assertEqual(response.status_code, 200)

	def test_get_book_with_id(self):
		"""test GET /<book_id> is empty and return 404"""
		tester = app.test_client(self)
		response = tester.get('/books/<book_id>', content_type='application/json')
		self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
	unittest.main()
