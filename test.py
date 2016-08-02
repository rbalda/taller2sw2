import unittest
from acceso import acceso, pagoExpreso
from tarjeta import Tarjeta

class SimpleTestCase(unittest.TestCase):
    def testA(self):
        tarjeta = Tarjeta("Leo", "Eras", "001024a", 2.50)
        assert acceso(tarjeta, "11:30:32", 2) == 0
        
    def testB(self):
        tarjeta = Tarjeta("Leo", "Eras", "00102345", 2.50)
        assert acceso(tarjeta, "11:30:32", 2) == 0
    
    def testC(self):
        tarjeta = Tarjeta("Leo", "Eras", "0010234", 2.50)
        assert acceso(tarjeta, "11:30:32", -1) == 0

    def testD(self):
        tarjeta = Tarjeta("Leo", "Eras", "0010234", 2.50)
        assert acceso("0010234", "11:30:32", 8) == 0

    def testE(self):
        tarjeta = Tarjeta("Leo", "Eras", "0010234", 2.50)
        assert acceso(tarjeta, "11:30:32", 2) == 1

    def testF(self):
        tarjeta = Tarjeta("Leo", "Eras", "0010234", 2.50)
        assert acceso(tarjeta, "09:30:32", 7) == 0

    def testG(self):
        tarjeta = Tarjeta("Leo", "Eras", "0010234", 2.50)
        assert acceso(tarjeta, "16:30:32", 7) == 0

    def testH(self):
        tarjeta = Tarjeta("Leo", "Eras", "0010234", 2.50)
        assert acceso(tarjeta, "11:30:32", 7) == 1

    def testI(self):
        tarjeta = Tarjeta("Leo", "Eras", "0110234", 2.50)
        assert acceso(tarjeta, "07:30:32", 1) == 0

    def testJ(self):
        tarjeta = Tarjeta("Leo", "Eras", "0110234", 2.50)
        assert acceso(tarjeta, "11:30:32", 1) == 1

    def testK(self):
        tarjeta = Tarjeta("Leo", "Eras", "0110234", 2.50)
        assert acceso(tarjeta, "19:30:32", 1) == 0

    def testL(self):
        tarjeta = Tarjeta("Leo", "Eras", "0110234", 2.50)
        assert acceso(tarjeta, "11:30:32", 7) == 0

    def testM(self):
        tarjeta = Tarjeta("Leo", "Eras", "0110234", 2.50)
        assert pagoExpreso(tarjeta, 6) == 0

    def testN(self):
        tarjeta = Tarjeta("Leo", "Eras", "0110234", 2.50)
        assert pagoExpreso(tarjeta, -1) == 0

    def testO(self):
        tarjeta = Tarjeta("Leo", "Eras", "0110234", 2.50)
        assert pagoExpreso(tarjeta, 5) == 1

    def testP(self):
        tarjeta = Tarjeta("Leo", "Eras", "01102341", 2.50)
        assert pagoExpreso(tarjeta, 3) == 0

        
if __name__ == "__main__":
    unittest.main()
