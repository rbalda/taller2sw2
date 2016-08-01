import unittest
import pytest
from Programa import Programa

class pruebas(unittest.TestCase):
    def test_function_1(self):
        programa = Programa()
        valor1 = programa.verificar_acceso("12345a", 1,8)
        valor2 = "Acceso Denegado"
        self.assertEqual(valor1, valor2)
    def test_function_2(self):
        programa = Programa()
        valor1 = programa.verificar_acceso("123456", 1,8)
        valor2 = "Acceso Denegado"
        self.assertEqual(valor1, valor2)
    def test_function_3(self):
        programa = Programa()
        valor1 = programa.verificar_acceso("1234567", 0,8)
        valor2 = "Acceso Denegado"
        self.assertEqual(valor1, valor2)
    def test_function_4(self):
        programa = Programa()
        valor1 = programa.verificar_acceso("0012345", 1,1)
        valor2 = "Acceso Concedido"
        self.assertEqual(valor1, valor2)
    def test_function_5(self):
        programa = Programa()
        valor1 = programa.verificar_acceso("0012345", 6,20)
        valor2 = "Acceso Denegado"
        self.assertEqual(valor1, valor2)
    def test_function_6(self):
        programa = Programa()
        valor1 = programa.verificar_acceso("1212345", 1,10)
        valor2 = "Acceso Concedido"
        self.assertEqual(valor1, valor2)
    def test_function_7(self):
        programa = Programa()
        valor1 = programa.verificar_acceso("1212345", 5,20)
        valor2 = "Acceso Denegado"
        self.assertEqual(valor1, valor2)

if __name__ == '__main__':
    unittest.main()
