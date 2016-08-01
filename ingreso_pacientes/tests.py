from django.test import TestCase

# Create your tests here.
from capital import Prestamo

# Creando casos de prueba
class CrearPrestamo(TestCase):

	def crear_prestamo(self):
		self.prestamo = Prestamo()

	def test_prestamo_inferior_a_5000_mes_invalido(self):
		total = self.crear_prestamo().valor_total(2000, 4)
		self.assertTrue(total, 2080.8)

	def test_prestamo_inferior_a_5000_mes_valido(self):
		total = self.crear_prestamo().valor_total(2000, 3)
		self.assertTrue(total, 2101.2)

	def test_prestamo_entre_5000_mes_invalido(self):
		total = self.crear_prestamo().valor_total(5000, 7)
		self.assertTrue(total, None)

	def test_prestamo_entre_10000_mes_invalido(self):
		total = self.crear_prestamo().valor_total(10000, 14)
		self.assertTrue(total, None)

    def test_prestamo_entre_10000_mes_valido(self):
		total = self.crear_prestamo().valor_total(10000, 12)
		self.assertTrue(total, 12272.0)

	def test_prestamo_mayor_20000(self):
		total = self.crear_prestamo().valor_total(21000, 1)
		self.assertTrue(total, None)