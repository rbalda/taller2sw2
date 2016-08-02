import unittest
from Programa import Programa

class pruebas(unittest.TestCase):

    #Si la tarjeta es válida entonces puede realizar el pago
    def test_integration1_module_1_3(self):
        programa = Programa()
        tarjeta = ["0012345", "AAA", 1.0]
        valor1 = programa.modulo_1_verificar_tarjeta(tarjeta[0])
        valor2 = True
        self.assertEqual(valor1[0], valor2) #Verifica que la tarjeta es válida

        valor3 = programa.modulo_3_sistema_pagos(tarjeta, 5)
        valor4 = "Pasaje cobrado exitosamente"
        self.assertEqual(valor3, valor4)
    #Si la tarjeta es inválida no puede realizar el pago
    def test_integration2_module_1_3(self):
        programa = Programa()
        tarjeta = ["00123", "AAA", 1.0]
        valor1 = programa.modulo_1_verificar_tarjeta(tarjeta[0])
        valor2 = False
        self.assertEqual(valor1[0], valor2) #Verifica que la tarjeta es inválida

        valor3 = programa.modulo_3_sistema_pagos(tarjeta, 5)
        valor4 = "No se pudo cobrar el pasaje"
        self.assertEqual(valor3, valor4)

    #Si la tarjeta es válida(empleado) y  todos los datos de día y hora son permitidos para el empleado, se permite el acceso
    def test_integration2_module_1_2(self):
        programa = Programa()
        tarjeta = "0012345"
        valor1 = programa.modulo_1_verificar_tarjeta(tarjeta)
        valor2 = True
        self.assertEqual(valor1[0], valor2) #Verifica que la tarjeta es válida

        valor3 = programa.modulo_2_acceso_valido(valor1[1], 2, 3)
        valor4 = True
        self.assertEqual(valor3, valor4) # Verifica que el acceso fue concedido
    #Si la tarjeta es inválida y  todos los datos de día y hora son permitidos no se permite el acceso
    def test_integration3_module_1_2(self):
        programa = Programa()
        tarjeta = "001234"
        valor1 = programa.modulo_1_verificar_tarjeta(tarjeta)
        valor2 = False
        self.assertEqual(valor1[0], valor2) #Verifica que la tarjeta es inválida

        valor3 = programa.modulo_2_acceso_valido(valor1[1], 2, 3)
        valor4 = False
        self.assertEqual(valor3, valor4) # Verifica que el acceso no fue concedido


if __name__ == '__main__':
    unittest.main()
