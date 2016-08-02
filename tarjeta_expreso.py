class Tarjeta:
	def __init__(self, nombres, apellidos, code, money):
		self.nombres_portador = nombres
		self.apellido_portador = apellidos
		self.codigo = code
		self.saldo = money

def cobrar_pasaje(permiso, dia, tarjeta):

	dias_no_gratis = {"Lunes", "Martes", "Miercoles", "Jueves", 1, 2, 3, 4}
	dias_gratis = {"Viernes", 5}
	personas_no_gratis = {"trabajador", "estudiante"}
	if (dia in dias_no_gratis):
		if permiso in personas_no_gratis:
			if tarjeta.saldo >= 0.25:
				tarjeta.saldo -= 0.25
				return 1
			else:
				return 0
		else:
			return 1
	elif (dia in dias_gratis):
		return 1