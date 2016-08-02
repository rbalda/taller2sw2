

class CodigoTarjeta():
	def checkCodigo(self,codigo):
		if not str(codigo).isdigit():
			return [False,None]

		if len(str(codigo))!=7:
			return [False,None,codigo]
		#check if empleado o aumno
		if str(codigo)[:2]=="00":
			return [True,"Empleado",codigo]

		return [True,"Estudiante",codigo]