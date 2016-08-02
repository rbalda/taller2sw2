from tarjeta import Tarjeta

class Cobrar():
	def cobrar_pasaje(self, tarjeta, dia):
		if (1 <= dia <= 4 and tarjeta.saldo >= 0.25):
			tarjeta.saldo -= 0.25
			print ("cobrado 0.25, saldo total: "+str(tarjeta.saldo))
			return 1
		elif (1 <= dia <= 4 and 0.0 <= tarjeta.saldo < 0.25):
			print ("saldo insuficiente, saldo total: "+str(tarjeta.saldo))
			return 0
		elif (dia == 5 and tarjeta.saldo >= 0.0):
			print ("cobrado 0.0, saldo total: "+str(tarjeta.saldo))
			return 1
		elif (dia > 5 or dia < 1):
			print ("error dia invalido: solo lunes a viernes")
			return 0
		elif (tarjeta.saldo < 0.0):
			print ("saldo invalido")
			return 0