from access_control import insert_day_and_hour
from CardValidator import validate
import unittest

class TestSystem(unittest.TestCase):

    def setUp(self):
        pass

    def test_code_employee(self):
        response = validate("0012345")[0]
        self.assertEqual(response,True)

    def test_code_student(self):
        response = validate("1234567")[0]
        self.assertEqual(response,True)

    def test_code_with_letter(self):
        response = validate("123a567")[0]
        self.assertEqual(response,False)

    def test_code_less_digits(self):
        response = validate("123456")[0]
        self.assertEqual(response,False)

    def test_code_more_digits(self):
        response = validate("12345678")[0]
        self.assertEqual(response,False)

    def test_valid_day_and_hour(self):
        self.assertEqual(insert_day_and_hour("1","12:00"),True)

    def test_invalid_day_number(self):
        self.assertEqual(insert_day_and_hour("8","12:00"),False)

    def test_invalid_day_string(self):
        self.assertEqual(insert_day_and_hour("lunes","12:00"),False)

    def test_invalid_Hour(self):
        self.assertEqual(insert_day_and_hour("1","32:00"),False)


if __name__ == '__main__':
    unittest.main()