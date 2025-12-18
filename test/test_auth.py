import unittest
from src.utils.security import hash_password, verify_password

class TestAuthLogic(unittest.TestCase):

    def test_password_hash_and_verify(self):
        password = "123456"
        hashed = hash_password(password)
        result = verify_password(hashed, password)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
