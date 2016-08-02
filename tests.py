import unittest
# import Tarjeta
from Tarjeta import Tarjeta
from Access import Access

class TestStringMethods(unittest.TestCase):
    def test_Tarjeta1(self):
        t = Tarjeta();
        self.assertEqual(t.isValid("0012345"), True)
    def test_Tarjeta2(self):
        t = Tarjeta();
        self.assertEqual(t.isValid("001234567890"), False)
    def test_Tarjeta3(self):
        t = Tarjeta();
        self.assertEqual(t.isValid("1234567"), True)
    def test_Tarjeta1(self):
        t = Tarjeta();
        self.assertEqual(t.isValid("0012345"), True)

    # student
    def test_Acceso1(self):
        acc = Access()
        self.assertEqual(acc.getAccess('8812345', 1, 18), '01')
    def test_Acceso2(self):
        acc = Access()
        self.assertEqual(acc.getAccess('8812345', 1, 19), '00')
    def test_Acceso3(self):
        acc = Access()
        self.assertEqual(acc.getAccess('8812345', 7, 18), '00')

    # employed
    def test_Acceso4(self):
        acc = Access()
        self.assertEqual(acc.getAccess('0012345', 1, 23), '01')
    def test_Acceso5(self):
        acc = Access()
        self.assertEqual(acc.getAccess('0012345', 6, 10), '01')
    def test_Acceso6(self):
        acc = Access()
        self.assertEqual(acc.getAccess('0012345', 6, 9), '00')

    def test_Acceso7(self):
        acc = Access()
        self.assertEqual(acc.getAccess('0012345', 8, 9), '00')
    def test_Acceso8(self):
        acc = Access()
        self.assertEqual(acc.getAccess('0012345', 8, 25), '00')


if __name__ == '__main__':
    unittest.main()
