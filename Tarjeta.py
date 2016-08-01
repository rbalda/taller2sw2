
class Tarjeta:

    def obtener_hora(self,hora):
        h = int(hora[0])
        h1 = (hora[1])
        return  h*10 + h1

    def obtener_minutos(self,hora):
        h = int(hora[3])
        h1 = (hora[4])
        return  h*10 + h1

    def validar_tarjetas(self,usuario,codigo,tiempo,dia):
        hora = self.obtener_hora(tiempo)
        minutos = self.obtener_minutos(tiempo)
        if(len(codigo)==7):
              if(usuario == "TRABAJADOR"):
                if(codigo[0]=="0" and codigo[1]=="0"):
                  if(dia == "LUNES" or dia== "MARTES"or dia == "MIERCOLES" or dia== "JUEVES" or dia == "VIERNES"):
                        return 1
                  elif(dia== "SABADO" or dia=="DOMINGO"):
                        if(hora < 10 or hora > 15):
                          return None
                        if(10 < hora < 15):
                            return 2
                else:
                  print("El codigo que ingreso es incorrecto.")
                  return None
              if(usuario == "ESTUDIANTE"):
                  if(codigo[0]!="0" and codigo[1]!="0"):
                      if(dia == "LUNES" or dia== "MARTES"or dia == "MIERCOLES" or dia== "JUEVES" or dia == "VIERNES"):
                           if(hora < 8 or hora > 18):
                            return None
                           if(8 < hora < 18):
                            return 1
                      else:
                            return None

        else:
              print("El codigo que ingreso es incorrecto.")
              return None

    def abrir_puerta(self, numacceso):

         if(numacceso==1 or numacceso==2):  #ACCESO CONCEDIDO
             return 1
         else:                              #ACCESO DENEGADO
             return 0