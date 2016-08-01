

import unittest
from tarjetas_class import Tarjeta

class Test(unittest.TestCase):
    def test1(self):  #codigo de acceso valor entero
        t = Tarjeta()
        self.assertEquals(t.esHorarioValido('0012345', 1, 10), 1)

    def test2(self):  #codigo de acceso valor entero de 7 digitos
        t = Tarjeta()
        self.assertEquals(t.esHorarioValido('0012345', 1, 10), 1)

    def test3(self):  #codigo de acceso valor entero no tiene 7 digitos
        t = Tarjeta()
        self.assertEquals(t.esHorarioValido('00123', 1, 10), 0)

    def test4(self):  #codigo de acceso valor entero
        t = Tarjeta()
        self.assertEquals(t.esHorarioValido('0012345', 1, 10), 1)

    def test5(self):  #codigo de acceso no es valor entero
        t = Tarjeta()
        self.assertEquals(t.esHorarioValido('hola', 1, 10), 0)

    def test6(self):  #dia valor entero
        t = Tarjeta()
        self.assertEquals(t.esHorarioValido('1012345', 1, 10), 1)

    def test7(self):  #dia valor ENTERO ENTre 1 y 7
        t = Tarjeta()
        self.assertEquals(t.esHorarioValido('1012345', 1, 6), 0)

    def test8(self):  #dia menor a 1
        t = Tarjeta()
        self.assertEquals(t.esHorarioValido('0012345', 0, 10), 0)

    def test9(self):  #dia no está entre 1 y 7
        t = Tarjeta()
        self.assertEquals(t.esHorarioValido('0012345', 0, 10), 0)

    def test10(self):  #dia mayor a 7
        t = Tarjeta()
        self.assertEquals(t.esHorarioValido('0012345', 10, 10), 0)

    def test11(self):  #hora entre 24 horas
        t = Tarjeta()
        self.assertEquals(t.esHorarioValido('0012345', 1, 10), 1)

    def test12(self):  #hora no está entre 24 horas
        t = Tarjeta()
        self.assertEquals(t.esHorarioValido('0012345', 10, 24), 0)



if __name__ == '__main__':
    unittest.main()





