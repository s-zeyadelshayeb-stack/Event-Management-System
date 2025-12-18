import unittest
from app import create_app
from src.repositories.user_repo import get_user_by_email

class TestUserRepository(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_user_not_found(self):
        user = get_user_by_email("fake@email.com")
        self.assertIsNone(user)

if __name__ == "__main__":
    unittest.main()
