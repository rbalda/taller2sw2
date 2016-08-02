class Acceso():
	def validar(self,codigo):

		if not (codigo.isdigit()):
			return "error"
		if (len(codigo) != 7):
			print str(codigo)
			return "error"
		if (codigo[:2] == "00"):
			return "empleado"
		else:
			return "estudiante"

	def acceso(self, tipo, hora, dia):
		_hour = hora.split("h")
		if(tipo == "estudiante" and dia >=1 and dia <=5 ):
			if(int(_hour[0]) >= 8 and int(_hour[0]) <= 18):
				if(int(_hour[0]) == 18 and int(_hour[1]) > 0):
					return 0
				else:
					return 1
			else:
				return 0
		elif (tipo == "empleado"):
			if (dia == 6 or dia == 7):
				if(int(_hour[0]) >= 10 and int(_hour[0]) <= 15):
					if(int(_hour[0]) == 15 and int(_hour[1]) > 0):
						return 0
					else:
						return 1
				else:
					return 0
			else:
				return 1
		else:
			return 0
