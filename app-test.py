from app import Books
import unittest


class HelloBooksTestCases(unittest.TestCase):

	def test_get_function(self):
		"""Should return get function"""
		result = Books.get(self)
		self.assertEqual(result, Books.get(self))


if __name__ == "__main__":
	unittest.main()
