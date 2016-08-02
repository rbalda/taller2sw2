import unittest
import acceso
import tarjeta
from tarjeta_expreso import Tarjeta
import tarjeta_expreso
# Create your tests here.
# Creando casos de prueba
class CrearPrestamo(unittest.TestCase):

	def test_crear_tarjeta(self):
		card = Tarjeta("f","e", 2,3)
		self.assertEqual(card.codigo, 2, None)

	def test_codigo_empleado_valido(self):
		permiso = tarjeta.validar_tarjeta(99999)
		self.assertEqual(permiso, "empleado", None)

	def test_codigo_estudiante_valido(self):
		permiso = tarjeta.validar_tarjeta(9999999)
		self.assertEqual(permiso, "estudiante", None)

	def test_codigo_invalido(self):
		permiso = tarjeta.validar_tarjeta(99999999)
		self.assertEqual(permiso, "invalido", None)

	def test_acceso_estudiante_dia_laboral(self):
		access = acceso.brindar_acceso("estudiante", 800, "Lunes")
		self.assertEqual(access, 1, None)

	def test_hora_invalida_estudiante_dia_laboral(self):
		access = acceso.brindar_acceso("estudiante", 1801, "Viernes")
		self.assertEqual(access, 0, None)

	def test_dia_invalido_estudiante_dia_laboral(self):
		access = acceso.brindar_acceso("estudiante", 1800, "Sabado")
		self.assertEqual(access, 0, None)

	def test_empleado_dia_laboral(self):
		access = acceso.brindar_acceso("empleado", 2359, "Martes")
		self.assertEqual(access, 1, None)

	def test_hora_invalida_empleado_dia_laboral(self):
		access = acceso.brindar_acceso("empleado", 2400, "Miercoles")
		self.assertEqual(access, 0, None)

	def test_empleado_fin_semana(self):
		access = acceso.brindar_acceso("empleado", 1000, "Domingo")
		self.assertEqual(access, 1, None)

	def test_empleado_fin_semana_hora_invalida(self):
		access = acceso.brindar_acceso("empleado", 959, "Domingo")
		self.assertEqual(access, 0, None)

	def test_empleado_fin_semana_dia_invalido(self):
		access = acceso.brindar_acceso("empleado", 1500, "Enero")
		self.assertEqual(access, 0, None)

	def test_permiso_invalido(self):
		access = acceso.brindar_acceso("invalido", 1500, "Domingo")
		self.assertEqual(access, 0, None)

	def test_estudiante_con_saldo_valido_dia_no_gratis(self):
		card = Tarjeta("Fernando Emmanuel","Campaña Rojas", 9999999, 0.25)
		bus = tarjeta_expreso.cobrar_pasaje("estudiante", "Lunes", card)
		self.assertEqual(bus, 1, None)

	def test_estudiante_con_saldo_invalido_dia_no_gratis(self):
		card = Tarjeta("Fernando Emmanuel","Campaña Rojas", 9999999, 0.24)
		bus = tarjeta_expreso.cobrar_pasaje("estudiante", "Lunes", card)
		self.assertEqual(bus, 0, None)

	def test_empleado_dia_no_gratis(self):
		card = Tarjeta("Fernando Emmanuel","Campaña Rojas", 9999999, 0.24)
		bus = tarjeta_expreso.cobrar_pasaje("empleado", "Lunes", card)
		self.assertEqual(bus, 1, None)

	def test_estudiante_dia_gratis(self):
		card = Tarjeta("Fernando Emmanuel","Campaña Rojas", 9999999, 0.24)
		bus = tarjeta_expreso.cobrar_pasaje("empleado", "Viernes", card)
		self.assertEqual(bus, 1, None)

	def test_integracion_acceso_tarjeta_expreso(self):
		dia = "Lunes"
		card = Tarjeta("Fernando Emmanuel","Campaña Rojas", 9999999, 0.25)
		bus = tarjeta_expreso.cobrar_pasaje(tarjeta.validar_tarjeta(card.codigo), dia, card)
		self.assertEqual(bus, 1, None)

	def test_integracion_acceso_tarjeta(self):
		dia = "Lunes"
		card = Tarjeta("Fernando Emmanuel","Campaña Rojas", 9999999, 0.25)
		permiso = tarjeta.validar_tarjeta(card.codigo)
		access = acceso.brindar_acceso(permiso, 1000, dia)
		self.assertEqual(access, 1, None)

if __name__ == "__main__":
	unittest.main()