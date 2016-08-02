import unittest

from ValidarTarjeta import Tarjeta
from Acceso import Acceso


class AccesoTestCase(unittest.TestCase):

    def setUp(self):
        self.tarjeta = Tarjeta()
        self.acceso = Acceso()

    #caso de ´prueba: tamaño del codigo < 7
    def test_1(self):
        self.assertEquals(self.acceso.getAcceso(
                self.tarjeta.validarTarjeta("2324"),0,1)
                ,0)
    #caso de ´prueba: tamaño del codigo = 7, tipo = Empleado(00), dia=5(sabado), hora=10
    def test_2(self):
        self.assertEquals(self.acceso.getAcceso(
                self.tarjeta.validarTarjeta("0024234"),5,10)
                ,1)

    #caso de ´prueba: tamaño del codigo = 7, tipo = Estudiante, dia=1(lunes), hora=11
    def test_3(self):
        self.assertEquals(self.acceso.getAcceso(
                self.tarjeta.validarTarjeta("23249283"),1,11)
                ,1)

    #caso de ´prueba: tamaño del codigo = 7, tipo = Estudiante, dia=string, string
    def test_4(self):
        self.assertEquals(self.acceso.getAcceso(
                self.tarjeta.validarTarjeta("2324234"),"lunes","10")
                ,0)

    #caso de ´prueba: tamaño del codigo = 7, tipo = Estudiante, dia=1(martes), hora=7
    def test_5(self):
        self.assertEquals(self.acceso.getAcceso(
                self.tarjeta.validarTarjeta("23249283"),1,7)
                ,0)

    #caso de ´prueba: tamaño del codigo = 7, tipo = Estudiante, dia=5(sabado), hora=7
    def test_6(self):
         self.assertEquals(self.acceso.getAcceso(
                self.tarjeta.validarTarjeta("23249283"),5,7)
                ,0)

    #caso de ´prueba: tamaño del codigo = 7, tipo = Empleado(00), dia=5(sabado), hora=6
    def test_7(self):
        self.assertEquals(self.acceso.getAcceso(
                self.tarjeta.validarTarjeta("0024234"),5,6)
                ,0)

    #caso de ´prueba: tamaño del codigo = 7, tipo = Empleado(00), dia=0(lunes), hora=6
    def test_8(self):
        self.assertEquals(self.acceso.getAcceso(
                self.tarjeta.validarTarjeta("0024234"),0,6)
                ,1)
    
    #caso de ´prueba: codigo como entero
    def test_9(self):
        self.assertEquals(self.acceso.getAcceso(
                self.tarjeta.validarTarjeta(0024234),0,6)
                ,0)


if __name__ == "__main__":
    unittest.main()
