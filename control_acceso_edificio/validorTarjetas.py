class Validador():
	"""
	Autor: Jorge Ayala
	Determina el tipo de tarjeta, ie :
	estudiante o empleado
	"""
	def respuesta(self,idTarjeta,edad,altura,genero):
                '''
                tarjeta: C10
                EDAD: CE1
                ALTURA: CE4
                GENERO: CE8
                '''
                if(idTarjeta[0] == '0' and  idTarjeta[1] == '0'):
                        edadValida = edad >= 18 and edad <= 100
                        alturaValida = altura > 100 and altura < 300
                        generoValido = genero == 0 or genero == 1
                        if(edadValida and alturaValida and generoValido):
                                return 'EST'
                        else:
                                return None
                else:
                        edadValida = edad >= 18 and edad <= 100
                        alturaValida = altura > 100 and altura < 300
                        generoValido = genero == 0 or genero == 1
                        if(edadValida and alturaValida and generoValido):
                                return 'EMP'
                        else:
                                return None

                        
                        
                
