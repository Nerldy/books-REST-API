from app import app

import unittest


class HelloBooksAPITestCase(unittest.TestCase):
	"""Class represents Hello Books test cases"""

	def test_book_creation(self):
		"""Test POST /books will create a book"""
		pass


if __name__ == '__main__':
	unittest.main()
