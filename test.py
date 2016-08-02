from access_control import validate_day_and_hour
from CardValidator import validate
from Card import Card
from ExpressPayment import payment
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
        self.assertEqual(validate_day_and_hour("employee","1","12:00"),True)

    def test_invalid_day_number(self):
        self.assertEqual(validate_day_and_hour("employee","8","12:00"),False)

    def test_invalid_day_string(self):
        self.assertEqual(validate_day_and_hour("employee","lunes","12:00"),False)

    def test_invalid_Hour(self):
        self.assertEqual(validate_day_and_hour("employee","1","32:00"),False)

    def test_restricted_hour_weekend_employee_day(self):
        self.assertEqual(validate_day_and_hour("employee","6","09:00"),False)

    def test_restricted_hour_weekend_employee_night(self):
        self.assertEqual(validate_day_and_hour("employee","6","18:00"),False)

    def test_restricted_day_weekend_student(self):
        self.assertEqual(validate_day_and_hour("student","6","09:00"),False)

    def test_restricted_hour_week_student_day(self):
        self.assertEqual(validate_day_and_hour("student","1","07:59"),False)

    def test_restricted_hour_week_student_night(self):
        self.assertEqual(validate_day_and_hour("student","1","19:00"),False)

    def test_valid_payment_monday_to_thursday(self):
        card = Card()
        card.credit=0.50
        self.assertEqual(payment(1,card),1)

    def test_valid_payment_friday(self):
        card = Card()
        self.assertEqual(payment(5,card),1)

    def test_invalid_payment_monday_to_thursday(self):
        card = Card()
        card.credit=0
        self.assertEqual(payment(1,card),0)

if __name__ == '__main__':
    unittest.main()