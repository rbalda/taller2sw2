from validorTarjetas import Validador

class sistemaPago():
	"""
	Autor: Jorge Ayala
	
	"""
	def respuesta(self,apellido,nombre,idTarjeta,saldo,dia):
                validar = Validador()
                tipoUsuario = validar.respuesta(idTarjeta,24,181,0)
                if(dia >= 1 and dia <=4):
                        if(saldo >= 0.25):
                                saldo = saldo - 0.25
                                return 1
                        else:
                                return 0
                elif(dia == 5):
                        return 1
                else:
                        return 0
                                
                        
                
                        
            
