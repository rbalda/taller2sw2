class Tarjeta:
	def __init__(self, tarjeta, tipo_empleado):
		self.tarjeta = tarjeta
		self.tipo_empleado = tipo_empleado

	# false or true Valid or invalid
	def validarLongitud(self):
		size = len(self.tarjeta)
		if(size != 7):
			return False
		return True

	def validarDigitos(self):
		for digit in self.tarjeta:
			if(digit.isdigit() == False):
				return False
		return True

	# false or true
	def verificarEstudiante(self):
		if(int(self.tarjeta[0]) == 0 and int(self.tarjeta[1]) == 0):
			return True
		return False


	# false or true Valid or invalid
	def validarUsuario(self):
		if(self.validarLongitud() == False):
			return False
		if(self.validarDigitos() == False):
			return False 
		else:
			if(self.tipo_empleado == "Estudiante"):
				return self.verificarEstudiante()

			elif(self.tipo_empleado == "Empleado"):
				if(self.verificarEstudiante() == True):
					return False
				return True