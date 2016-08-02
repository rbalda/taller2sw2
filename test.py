import unittest
from mod_access import Acceso

class TestFinanciero(unittest.TestCase):
    def setUp(self):
        self.acceso = Acceso()
    def test_1(self):
        self.assertEqual(self.acceso.checkAccess('1234567',2,'12h15'),1)
    def test_2(self):
        self.assertEqual(self.acceso.checkAccess('1234567',6,'16h15'),0)
    def test_3(self):
        self.assertEqual(self.acceso.checkAccess('12345673',3,'16h15'),0)
    def test_4(self):
        self.assertEqual(self.acceso.checkAccess('0034567',6,'16h15'),0)
    def test_5(self):
        self.assertEqual(self.acceso.checkAccess('0034567',2,'19h15'),1)
    def test_6(self):
        self.assertEqual(self.acceso.checkAccess('a034567',2,'19h15'),0)
    def test_7(self):
        self.assertEqual(self.acceso.checkAccess('0034567',10,'19h15'),0)
    def test_7(self):
        self.assertEqual(self.acceso.checkAccess('0034567',2,'219h15'),0)
    def test_7(self):
        self.assertEqual(self.acceso.checkAccess('0034567',2,'1915'),0)

if __name__ == '__main__':
	unittest.main()