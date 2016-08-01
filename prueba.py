import unittest
from codigo import Control

class AddTest(unittest.TestCase):
    def setUp(self):
      self.codigo = Control()
      pass
    def tearDown(self):
      pass

    def test_codigoEmpiezaDobleCero(self):
        self.assertEqual(self.codigo.valor_acceso('0012345',1, 1),None)

    def test_codigoNOEmpiezaDobleCero(self):
        self.assertEqual(self.codigo.valor_acceso('1234567',1, 1),None)
    def test_codigoIncorrecto(self):
        self.assertEqual(self.codigo.valor_acceso('12345675',1, 1),None)
    def test_codigoIncorrecto2(self):
        self.assertEqual(self.codigo.valor_acceso('12345',1, 1),None)
    def test_diaTrabajador(self):
        self.assertEqual(self.codigo.valor_acceso('0021234',4, 1),None)

if __name__=='__main__':
   unittest.main()
