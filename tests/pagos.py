from acceso import Acceso
from modulo_tarjeta import Tarjeta
class Pago:
	def __init__(self, acceso):
		self.acceso = acceso
		self.pasaje = 0

	def checkPagoARealizar(self):
		if(self.acceso.dia in range(1,5)):
			self.pasaje = 0.25
		elif(self.acceso.dia == 5):
			self.pasaje = 0
		return self.pasaje

	def realizarPago(self):
		if(self.acceso.dia in range(6,8) or self.acceso.dia > 7 or self.acceso.dia < 1):
			return False

		if(self.acceso.tarjeta.saldo < 0):
			return False
		if (self.checkPagoARealizar() == 0):
			return True
		elif (self.acceso.tarjeta.saldo < 0.25):
			return False
		elif (self.acceso.tarjeta.saldo >= 0.25 ):
			self.acceso.tarjeta.saldo = self.acceso.tarjeta.saldo - 0.25
			return True
