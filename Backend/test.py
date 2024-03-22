import unittest

from app import app

class FlaskTest(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get("/home")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_newsletter(self):
        tester = app.test_client(self)
        response = tester.get("news_letter")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)



if __name__ == '__main__':
    unittest.main()