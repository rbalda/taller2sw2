def brindar_acceso(permiso, hora, dia):
	dia_laborables = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes"}
	fin_de_semana = {"Sabado", "Domingo"}
	if(permiso == "estudiante"):
		if (dia in dia_laborables):
			if (hora >= 800 and hora <= 1800):
				return 1
			else:
				return 0
		else:
			return 0
	elif(permiso == "empleado"):
		if (dia in dia_laborables):
			if (hora >= 0000 and hora < 2400):
				return 1
			else:
				return 0
		elif (dia in fin_de_semana):
			if (hora >= 1000 and hora <= 1500):
				return 1
			else:
				return 0
		else:
			return 0
	else:
		return 0