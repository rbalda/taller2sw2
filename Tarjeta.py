
class Tarjeta:

    nombre = ""
    apellido = ""
    codigo = ""
    saldo = 0.0

    def __init__(self,nombre,apellido,codigo,saldo):
        self.nombre = nombre
        self.apellido = apellido
        self.codigo = codigo
        self.saldo = saldo

    def obtener_hora(self,hora):
        h = int(hora[0])
        h1 = int(hora[1])
        return  h*10 + h1
        
    def validar_tarjetas(self,usuario,codigo,tiempo,dia):
        hora = self.obtener_hora(tiempo)
        #minutos = self.obtener_minutos(tiempo)
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

    def pago_pasaje(self, acceso, dia, valorTarjeta):
        pasaje= 0.25
        if(acceso==1):
            if(dia == "LUNES" or dia== "MARTES"or dia == "MIERCOLES" or dia== "JUEVES"):
                saldo = valorTarjeta - pasaje
                if(saldo >= 0):
                    self.saldo = saldo
                    print(self.saldo)
                    return 1
                else:
                    return 0
            elif(dia== "VIERNES"):
                return 1
            else:
              print("El codigo que ingreso es incorrecto.")
              return 0
        else:
            return 0
