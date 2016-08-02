from validorTarjetas import Validador
class Puerta():
	"""
	Autor: Jorge Ayala
	
	"""
	def respuesta(self,tipoUsuario,dia,hora):
                if(tipoUsuario == 'EST'):
                        diaLaborable = dia > 0 and dia < 6
                        horaEstudiante = hora in ['08h00','09h00','10h00','11h00','12h00','13h00','14h00','15h00','16h00','17h00','18h00']
                        if(diaLaborable and horaEstudiante):
                                return 1
                        else:
                                return 0

                elif(tipoUsuario == 'EMP'):
                        diaLaborable = dia > 0 and dia < 6
                        finDe = dia == 6 or dia == 7
                        horaFinSem = hora in ['10h00','11h00','12h00','13h00','14h00','15h00']
                        horaValida = hora in ['00h00','01h00','02h00','03h00','04h00','05h00','06h00','07h00','08h00','09h00','10h00','11h00','12h00','13h00','14h00','15h00','16h00','17h00','18h00','19h00','20h00','21h00','22h00','23h00']
                        if(finDe and horaFinSem):
                                return 1
                        elif(diaLaborable and horaValida):
                                return 1
                        else:
                                return 0
                else:
                        return 0
                        
            
