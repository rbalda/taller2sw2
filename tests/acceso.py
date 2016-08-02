from modulo_tarjeta import Tarjeta 
class Acceso:
	# dias 1 al 7
	def __init__(self, tarjeta, dia, hora):
		self.tarjeta = tarjeta
		self. dia = dia
		self.hora = hora

	def validarHorarioEmpleado(self):
		if(self.dia == 6 or self.dia == 7):
			if(self.hora >=10 and self.hora <= 15):
				return True
			else:
				return False
		else:
			return True

	def validarHorarioEstudiante(self):
		if(self.dia != 7 and self.dia != 6):
			if(self.hora >= 8 and self.hora <= 18):
				return True
			return False
		else:
			return False

	def validarHora(self):
		if(self.hora>24 or self.hora <0):
			return False
		return True

	def validarAcceso(self):
		if(isinstance(self.hora, str)):
			return False
		if(isinstance(self.dia, str)):
			return False
		if(self.hora>24 or self.hora <0):
			return False
		if(self.dia < 1 or self.dia >7):
			return False

		if(self.tarjeta.tipo_empleado == "Estudiante"):
			return self.validarHorarioEstudiante()
		elif(self.tarjeta.tipo_empleado == "Empleado"):
			return self.validarHorarioEmpleado()
