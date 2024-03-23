import unittest

from app import app

class FlaskTest(unittest.TestCase):
    #check if the response is 200
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get("/home")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_main(self):
        tester = app.test_client(self)
        response = tester.get("/main")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_explore(self):
        tester = app.test_client(self)
        response = tester.get("/explore")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    def test_newsletter(self):
        tester = app.test_client(self)
        response = tester.get("/news_letter")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_questionnaire(self):
        tester = app.test_client(self)
        response = tester.get("/questionnaire")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_quiz(self):
        tester = app.test_client(self)
        response = tester.get("/quiz")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_career(self):
        tester = app.test_client(self)
        response = tester.get("/career")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    def test_signin(self):
        tester = app.test_client(self)
        response = tester.get("/signin_form")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_signup(self):
        tester = app.test_client(self)
        response = tester.get("/signup_form")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    
     

if __name__ == '__main__':
    unittest.main()
