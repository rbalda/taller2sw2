import unittest
from acceso import Acceso
from modulo_tarjeta import Tarjeta
from pagos import Pago
class AccesoTestCase(unittest.TestCase):

    def setUp(self):
        """se la llama antes de cada test"""
        self.tarjeta = Tarjeta("0011112","Estudiante", "andres", "caceres", 0)
        self.acceso = Acceso(self.tarjeta, 6, 15)
        self.pago = Pago(self.acceso)

    def tearDown(self):
        """llamar luego de cada test"""
        print("termino test")

    def testPagoDiaMayorA7(self):
        self.tarjeta = Tarjeta("00222223","Estudiante", "andres","caceres",0.25)
        self.acceso = Acceso(self.tarjeta, 8, 25)
        self.pago = Pago(self.acceso)
        assert self.pago.realizarPago() == False

    def testPagoDiaEntre6y7(self):
        self.tarjeta = Tarjeta("00222223","Estudiante", "andres","caceres",0.25)
        self.acceso = Acceso(self.tarjeta, 7, 13)
        self.pago = Pago(self.acceso)
        assert self.pago.realizarPago() == False
        
    def testPagoDiaValido(self):
        self.tarjeta = Tarjeta("00222223","Estudiante", "andres","caceres",0.25)
        self.acceso = Acceso(self.tarjeta, 1, 13)
        self.pago = Pago(self.acceso)
        assert self.pago.realizarPago() == True

    def testSaldoNegativo(self):
        self.tarjeta = Tarjeta("00222223","Estudiante", "andres","caceres",-0.25)
        self.acceso = Acceso(self.tarjeta, 1, 13)
        self.pago = Pago(self.acceso)
        assert self.pago.realizarPago() == False
        
    def testSaldoPagoen0Viernes(self):
        self.tarjeta = Tarjeta("00222223","Estudiante", "andres","caceres",0.25)
        self.acceso = Acceso(self.tarjeta, 5, 13)
        self.pago = Pago(self.acceso)
        self.pago.realizarPago()
        assert self.pago.acceso.tarjeta.saldo == 0.25

    def testPagoEntreSemanaSaldoMenorAMinimo(self):
        self.tarjeta = Tarjeta("00222223","Estudiante", "andres","caceres",0.02)
        self.acceso = Acceso(self.tarjeta, 4, 13)
        self.pago = Pago(self.acceso)
        self.pago.realizarPago()
        assert self.pago.realizarPago() == False

    def testSaldoGrande(self):
        self.tarjeta = Tarjeta("00222223","Estudiante", "andres","caceres",0.50)
        self.acceso = Acceso(self.tarjeta, 4, 13)
        self.pago = Pago(self.acceso)
        self.pago.realizarPago()
        assert self.pago.acceso.tarjeta.saldo == 0.25

    
if __name__ == "__main__":
    unittest.main()   # run all tests
