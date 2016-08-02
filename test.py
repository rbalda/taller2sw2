import unittest
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
    def test_function_8(self):
        programa = Programa()
        valor1 = programa.verificar_acceso("1212345", 5,-1)
        valor2 = "Acceso Denegado"
        self.assertEqual(valor1, valor2)
    def test_function_9(self):
        programa = Programa()
        valor1 = programa.verificar_acceso("0012345", 6,11)
        valor2 = "Acceso Concedido"
        self.assertEqual(valor1, valor2)
    #Pruebas del módulo 3
    #Tarjeta = [Código, Nombre y apellido, Saldo]
    def test_function_10(self):
        programa = Programa()
        tarjeta = ["0012345", "AAA", 1.0]
        valor1 = programa.modulo_3_sistema_pagos(tarjeta, 5)
        valor2 = "Pasaje cobrado exitosamente"
        self.assertEqual(valor1, valor2)
    def test_function_11(self):
        programa = Programa()
        tarjeta = ["2212345", "AAA", 1.0]
        valor1 = programa.modulo_3_sistema_pagos(tarjeta, 2)
        valor2 = "Pasaje cobrado exitosamente"
        self.assertEqual(valor1, valor2)
    def test_function_12(self):
        programa = Programa()
        tarjeta = ["2212345", "AAA", 'a']
        valor1 = programa.modulo_3_sistema_pagos(tarjeta, 2)
        valor2 = "No se pudo cobrar el pasaje"
        self.assertEqual(valor1, valor2)
    def test_function_13(self):
        programa = Programa()
        tarjeta = ["2212345", "AAA", 0]
        valor1 = programa.modulo_3_sistema_pagos(tarjeta, 2)
        valor2 = "No se pudo cobrar el pasaje"
        self.assertEqual(valor1, valor2)
    def test_function_14(self):
        programa = Programa()
        tarjeta = ["2212345", "AAA", 0]
        valor1 = programa.modulo_3_sistema_pagos(tarjeta, 5)
        valor2 = "Pasaje cobrado exitosamente"
        self.assertEqual(valor1, valor2)
    def test_function_15(self):
        programa = Programa()
        tarjeta = ["2212345", "AAA", 1]
        valor1 = programa.modulo_3_sistema_pagos(tarjeta, 6)
        valor2 = "No se pudo cobrar el pasaje"
    def test_function_16(self):
        programa = Programa()
        tarjeta = ["2212345", "AAA", 1]
        valor1 = programa.modulo_3_sistema_pagos(tarjeta, 'a')
        valor2 = "No se pudo cobrar el pasaje"

if __name__ == '__main__':
    unittest.main()
