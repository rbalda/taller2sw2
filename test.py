import unittest
from Acceso import Acceso

class TestFinanciero(unittest.TestCase):
    def setUp(self):
        self.Acceso = Acceso()

    def test_1(self):
        self.assertEqual(self.Acceso.validar("0012345"), "empleado")

    def test_2(self):
        self.assertEqual(self.Acceso.validar("4312345"), "estudiante")

    def test_3(self):
        self.assertEqual(self.Acceso.validar("002312399"), "error")

    def test_4(self):
        self.assertEqual(self.Acceso.acceso(self.Acceso.validar("0023456"), "12h30", 2), 1)

    def test_5(self):
        self.assertEqual(self.Acceso.acceso(self.Acceso.validar("0012345"), "18h30", 6), 0)

    def test_6(self):
        self.assertEqual(self.Acceso.acceso(self.Acceso.validar("0012345"), "15h00", 6), 1)

    def test_7(self):
        self.assertEqual(self.Acceso.acceso(self.Acceso.validar("0012345"), "18h30", 6), 0)

    def test_8(self):
        self.assertEqual(self.Acceso.acceso(self.Acceso.validar("2212345"), "17h30", 4), 1)

    def test_9(self):
        self.assertEqual(self.Acceso.acceso(self.Acceso.validar("7712345"), "18h30", 1), 0)

if __name__ == '__main__':
	unittest.main()
