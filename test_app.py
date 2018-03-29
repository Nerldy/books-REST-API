from app import app, AllBooksResource
import unittest


class BooksAPITestCases(unittest.TestCase):

	def test_get_books(self):
		"""tests GET /books returns json ans 200 ok"""
		tester = app.test_client(self)
		response = tester.get('/books', content_type='application/json')
		self.assertEqual(response.status_code, 200)

	def test_get_a_book_returns_404(self):
		"""tests GET /book/<book_id> returns 404"""
		tester = app.test_client(self)
		response = tester.get('/books/1', content_type='application/json')
		self.assertEqual(response.status_code, 404)

	def test_post_book(self):
		"""tests POST /books/<book_id> returns 201"""
		tester = app.test_client(self)
		response = tester.post('/book/1', content_type='application/json')
		self.assertEqual(response.status_code, 201)

	def test_post_book_duplicate(self):
		"""tests POST /books/<book_id> returns 400 bad request"""
		tester = app.test_client(self)
		response1 = tester.post('/book/1', content_type='application/json')
		response2 = tester.post('/book/1', content_type='application/json')
		response = (response1.status_code == response2.status_code)
		self.assertEqual(response, True)


if __name__ == '__main__':
	unittest.main()
