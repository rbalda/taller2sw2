from mod_tarjeta import *

class Acceso():
	def checkAccess(self,codigo,dia,hora):
		#check if codigo es valido
		codigo = CodigoTarjeta().checkCodigo(codigo)
		if not codigo[0]:
			return 0;
		#el codigo es valido
		#es necesario chequear las horas con el dia
		if dia<1 or dia>8:
			return 0
		if len(str(hora))!=5:
			return 0
		hora = hora.split('h')
		if len(hora)!=2:
			return 0
		if int(hora[0])<0 or int(hora[0])>24 or int(hora[1])<0 or int(hora[1])>59:
			return 0
		if codigo[1]=="Empleado":

			if dia<6:
				#dias laborales
				return 1
			elif (int(hora[0])>=10 and int(hora[0])<15) or (int(hora[0])>=10 and int(hora[0])==15 and int(hora[1])==0):
				#fin de semana entre las 10 y las 15h00.
				return 1
			else:
				return 0
		else:
			#es estudiante
			if dia<6:
				if (int(hora[0])>=8 and int(hora[0])<18) or (int(hora[0])>=8 and int(hora[0])==18 and int(hora[1])==0):
					return 1
		return 0
