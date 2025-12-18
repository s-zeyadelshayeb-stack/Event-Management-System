import unittest
from app import create_app
from src.repositories.registration_repo import  register_user

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.ctx = self.app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

    def test_register_user(self):
        result =  register_user(student_id=1, event_id=1)
        self.assertTrue(result)

if __name__ == "_main_":
    unittest.main()