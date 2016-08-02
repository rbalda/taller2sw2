import unittest

from pasaje import Pasaje


class AddTest(unittest.TestCase):
    def setUp(self):
      self.pasaje = Pasaje()

      pass
    def tearDown(self):
      pass


    def test_cobrarPasajeLunes_Si_saldo(self):
        self.assertEqual(self.pasaje.valor_cobrar(1,0.25,1),1)
        
    def test_cobrarPasaje_Martes_NO_Saldo(self):
        self.assertEqual(self.pasaje.valor_cobrar(1,0.25,0),0)

    def test_cobrarPasaje_Viernes(self):
        self.assertEqual(self.pasaje.valor_cobrar(5,0.25,0),1)

    def test_cobrarPasaje_Sabado(self):
        self.assertEqual(self.pasaje.valor_cobrar(6,0.25,0),0)

  

if __name__=='__main__':
   unittest.main()
