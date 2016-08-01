import unittest
import acceso
import tarjeta
# Create your tests here.
# Creando casos de prueba
class CrearPrestamo(unittest.TestCase):

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

if __name__ == "__main__":
	unittest.main()