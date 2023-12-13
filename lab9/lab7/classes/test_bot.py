import unittest
from .validator import Validator
v = Validator()
class TestBot(unittest.TestCase):
    def test_validate_email(self):
        self.assertTrue(v.validate_email("test@example.com"))
        self.assertFalse(v.validate_email("test@example"))
        self.assertFalse(v.validate_email("test@.com"))

    def test_validate_color(self):
        self.assertTrue(v.validate_color("blue"))
        self.assertFalse(v.validate_color("turquoise"))

if __name__ == '__main__':
    unittest.main()