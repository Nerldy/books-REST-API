from app import app

import unittest


class BasicTestCase(unittest.TestCase):

	def test_index(self):
		"""
		:return: Hello World string
		"""
		tester = app.test_client(self)
		response = tester.get('/', content_type='html/text')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data, b'Hello World')

	def test_get_all_books(self):
		"""
		:return: get_all_books function
		"""
		tester = app.test_client(self)
		response = tester.get('/books', content_type='html/text')
		self.assertEqual(response.data, b"get all books")


if __name__ == '__main__':
	unittest.main()
