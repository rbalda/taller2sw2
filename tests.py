import unittest
from acceso import Acceso

class ValidarAcceso(unittest.TestCase):

	def test_validar_acceso_1(self):
		acceso = Acceso()
		self.assertEqual(acceso.validar_acceso("0012345", 10, 1) , 1)
	def test_validar_acceso_2(self):
		acceso = Acceso()
		self.assertEqual(acceso.validar_acceso("0012345",10,7), 1)
	def test_validar_acceso_3(self):
		acceso = Acceso()
		self.assertEqual(acceso.validar_acceso("1345678",10,1), 1)
	def test_validar_acceso_4(self):
		acceso = Acceso()
		self.assertEqual(acceso.validar_acceso("1345678",20,1), 0)
	
if __name__ == '__main__':
	unittest.main()