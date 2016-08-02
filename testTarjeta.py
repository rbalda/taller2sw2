import unittest
from tarjetas_class import Tarjeta


class Test(unittest.TestCase):
    def test1(self):  # codigo de acceso valor entero
        t = Tarjeta()
        t.setNumero("0012345")
        self.assertEquals(t.esHorarioValido(1, 10), 1)

    def test2(self):  # codigo de acceso valor entero de 7 digitos
        t = Tarjeta()
        t.setNumero("0012345")
        self.assertEquals(t.esHorarioValido(1, 10), 1)

    def test3(self):  # codigo de acceso valor entero no tiene 7 digitos
        t = Tarjeta()
        t.setNumero("00123")
        self.assertEquals(t.esHorarioValido(1, 10), 0)

    def test4(self):  # codigo de acceso valor entero
        t = Tarjeta()
        t.setNumero("0012345")
        self.assertEquals(t.esHorarioValido(1, 10), 1)

    def test5(self):  # codigo de acceso no es valor entero
        t = Tarjeta()
        t.setNumero("hola")
        self.assertEquals(t.esHorarioValido(1, 10), 0)

    def test6(self):  # dia valor entero
        t = Tarjeta()
        t.setNumero("1012345")
        self.assertEquals(t.esHorarioValido(1, 10), 1)

    def test7(self):  # dia valor ENTERO ENTre 1 y 7
        t = Tarjeta()
        t.setNumero("1012345")
        self.assertEquals(t.esHorarioValido(1, 6), 0)

    def test8(self):  # dia menor a 1
        t = Tarjeta()
        t.setNumero("0012345")
        self.assertEquals(t.esHorarioValido(0, 10), 0)

    def test9(self):  # dia no está entre 1 y 7
        t = Tarjeta()
        t.setNumero("0012345")
        self.assertEquals(t.esHorarioValido(0, 10), 0)

    def test10(self):  # dia mayor a 7
        t = Tarjeta()
        t.setNumero("0012345")
        self.assertEquals(t.esHorarioValido(10, 10), 0)

    def test11(self):  # hora entre 24 horas
        t = Tarjeta()
        t.setNumero("0012345")
        self.assertEquals(t.esHorarioValido(1, 10), 1)

    def test12(self):  # hora no está entre 24 horas
        t = Tarjeta()
        t.setNumero("0012345")
        self.assertEquals(t.esHorarioValido(10, 24), 0)

    def test13(self):
        t = Tarjeta()
        t.setAcceso(1)
        t.setSaldo(0)
        self.assertEquals(t.esPagoValido(5), 1)

    def test14(self):
        t = Tarjeta()
        t.setAcceso(1)
        t.setSaldo(0.5)
        self.assertEquals(t.esPagoValido(1), 1)

    def test15(self):
        t = Tarjeta()
        t.setAcceso(1)
        t.setSaldo(0)
        self.assertEquals(t.esPagoValido(1), 0)

    def test16(self):
        t = Tarjeta()
        t.setAcceso(1)
        t.setSaldo(0)
        self.assertEquals(t.esPagoValido(7), 0)

    def test17(self):
        t = Tarjeta()
        t.setAcceso(1)
        t.setSaldo(0)
        self.assertEquals(t.esPagoValido(1.5), 0)

    def test18(self):
        t = Tarjeta()
        t.setAcceso(1)
        t.setSaldo(-0.5)
        self.assertEquals(t.esPagoValido(1), 0)

    def test19(self):
        t = Tarjeta()
        t.setAcceso(1)
        t.setSaldo(0)
        self.assertEquals(t.esPagoValido(-1), 0)

    # Pruebas de integracion
    def test20(self):
        t = Tarjeta()
        t.setSaldo(1)
        t.setNumero("0012345")
        acceso = t.esHorarioValido(1,10)
        self.assertEquals(t.esPagoValido(1), 1)

    def test21(self):
        t = Tarjeta()
        t.setSaldo(0)
        t.setNumero("0012345")
        acceso = t.esHorarioValido(1,10)
        self.assertEquals(t.esPagoValido(1), 0)

    def test22(self):
        t = Tarjeta()
        t.setSaldo(1)
        t.setNumero("0012345")
        acceso = t.esHorarioValido(0,10)
        self.assertEquals(t.esPagoValido(1), 0)


if __name__ == '__main__':
    unittest.main()
