import unittest
from app import create_app
from src.repositories.feedback_repo import submit_feedback, get_user_feedback

class TestFeedback(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_submit_feedback(self):
        result = submit_feedback(
            student_id=1,
            event_id=1,
            rating=5,
            comment="Good event"
        )
        self.assertIsNotNone(result)

    def test_get_user_feedback(self):
        feedback = get_user_feedback(student_id=1, event_id=1)
       
        self.assertTrue(feedback is None or isinstance(feedback, dict))

if __name__ == "_main_":
    unittest.main()