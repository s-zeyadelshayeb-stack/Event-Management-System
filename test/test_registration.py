import unittest
from app import create_app
from src.repositories.registration_repo import register_user

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_register_user(self):
        result = register_user(student_id=1, event_id=1)
        
        self.assertTrue(result is None or isinstance(result, int))

if __name__ == "__main__":
    unittest.main()
