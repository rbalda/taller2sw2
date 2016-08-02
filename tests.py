import unittest
from acceso import Acceso
from tarjeta import Tarjeta
from cobrar import Cobrar

class ValidarAcceso(unittest.TestCase):
	#Acceso tests
	def test_validar_acceso_1(self):
		acceso = Acceso()
		tarjeta = Tarjeta("John", "Doe", "0012345", 2.5)
		self.assertEqual(acceso.validar_acceso(tarjeta.codigo, 10, 1) , 1)
	def test_validar_acceso_2(self):
		acceso = Acceso()
		tarjeta = Tarjeta("John", "Doe", "0012345", 2.5)
		self.assertEqual(acceso.validar_acceso(tarjeta.codigo, 10 ,7), 1)
	def test_validar_acceso_3(self):
		acceso = Acceso()
		tarjeta = Tarjeta("John", "Doe", "1345678", 2.5)
		self.assertEqual(acceso.validar_acceso(tarjeta.codigo, 10, 1), 1)
	def test_validar_acceso_4(self):
		acceso = Acceso()
		tarjeta = Tarjeta("John", "Doe", "1345678", 2.5)
		self.assertEqual(acceso.validar_acceso(tarjeta.codigo, 20, 1), 0)
	def test_validar_acceso_5(self):
		acceso = Acceso()
		tarjeta = Tarjeta("John", "Doe", "1111345678", 2.5)
		self.assertEqual(acceso.validar_acceso(tarjeta.codigo, 20, 1), 0)

	#Cobro tests
	def test_validar_cobro_1(self):
		tarjeta = Tarjeta("John", "Doe", "0012345", 2.5)
		cobrar = Cobrar()
		self.assertEqual(cobrar.cobrar_pasaje(tarjeta, 1), 1)
	def test_validar_cobro_2(self):
		tarjeta = Tarjeta("John", "Doe", "0012345", 0.1)
		cobrar = Cobrar()
		self.assertEqual(cobrar.cobrar_pasaje(tarjeta, 1), 0)
	def test_validar_cobro_3(self):
		tarjeta = Tarjeta("John", "Doe", "1112345", 2.5)
		cobrar = Cobrar()
		self.assertEqual(cobrar.cobrar_pasaje(tarjeta, 6), 0)
	def test_validar_cobro_4(self):
		tarjeta = Tarjeta("John", "Doe", "0012345", 0.1)
		cobrar = Cobrar()
		self.assertEqual(cobrar.cobrar_pasaje(tarjeta, 7), 0)
	def test_validar_cobro_5(self):
		tarjeta = Tarjeta("John", "Doe", "0012345", 0.0)
		cobrar = Cobrar()
		self.assertEqual(cobrar.cobrar_pasaje(tarjeta, 5), 1)
	def test_validar_cobro_6(self):
		tarjeta = Tarjeta("John", "Doe", "0012345", -0.5)
		cobrar = Cobrar()
		self.assertEqual(cobrar.cobrar_pasaje(tarjeta, 1), 0)

	#Integracion tests
	def test_integracion_1(self):
		tarjeta = Tarjeta("John", "Doe", "0012345", 2.5)
		cobrar = Cobrar()
		acceso = Acceso()
		valorCobrar = cobrar.cobrar_pasaje(tarjeta, 1)
		valorAcceso = acceso.validar_acceso(tarjeta.codigo, 10, 1)
		valido = valorCobrar * valorAcceso
		self.assertEqual(valido, 1)
	def test_integracion_2(self):
		tarjeta = Tarjeta("John", "Doe", "00012345", 2.5)
		cobrar = Cobrar()
		acceso = Acceso()
		valorCobrar = cobrar.cobrar_pasaje(tarjeta, 1)
		valorAcceso = acceso.validar_acceso(tarjeta.codigo, 10, 1)
		valido = valorCobrar * valorAcceso
		self.assertEqual(valido, 0)
	def test_integracion_3(self):
		tarjeta = Tarjeta("John", "Doe", "1112345", 2.5)
		cobrar = Cobrar()
		acceso = Acceso()
		valorCobrar = cobrar.cobrar_pasaje(tarjeta, 1)
		valorAcceso = acceso.validar_acceso(tarjeta.codigo, 20, 1)
		valido = valorCobrar * valorAcceso
		self.assertEqual(valido, 0)
	def test_integracion_4(self):
		tarjeta = Tarjeta("John", "Doe", "0012345", 0.1)
		cobrar = Cobrar()
		acceso = Acceso()
		valorCobrar = cobrar.cobrar_pasaje(tarjeta, 1)
		valorAcceso = acceso.validar_acceso(tarjeta.codigo, 10, 1)
		valido = valorCobrar * valorAcceso
		self.assertEqual(valido, 0)
	def test_integracion_5(self):
		tarjeta = Tarjeta("John", "Doe", "1112345", 0.1)
		cobrar = Cobrar()
		acceso = Acceso()
		valorCobrar = cobrar.cobrar_pasaje(tarjeta, 1)
		valorAcceso = acceso.validar_acceso(tarjeta.codigo, 10, 1)
		valido = valorCobrar * valorAcceso
		self.assertEqual(valido, 0)
	def test_integracion_6(self):
		tarjeta = Tarjeta("John", "Doe", "0012345", 2.5)
		cobrar = Cobrar()
		acceso = Acceso()
		valorCobrar = cobrar.cobrar_pasaje(tarjeta, 6)
		valorAcceso = acceso.validar_acceso(tarjeta.codigo, 20, 1)
		valido = valorCobrar * valorAcceso
		self.assertEqual(valido, 0)
if __name__ == '__main__':
	unittest.main()