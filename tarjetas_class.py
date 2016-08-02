
class Tarjeta():

    nombres = ""
    apellidos = ""
    numero = ""
    saldo = 0
    acceso = 0

    def setSaldo(self, valor):
        self.saldo = valor

    def setNumero(self, valor):
        self.numero = valor

    def setAcceso(self, valor):
        self.acceso = valor

    def get_Tipo_Tarjeta(self):
        if(self.numero.isdigit()): # Only digit in this string
            if(len(self.numero) == 7):
                if(self.numero[0] == '0' and self.numero [1] == '0'):
                    return "Empleado"
                else:
                    return "Estudiante"
        return "Invalido"

    def esHorarioValido(self, dia, hora):
        if(self.get_Tipo_Tarjeta() == "Estudiante"):
            if(hora >= 8 and hora <= 18 and (dia == 1 or dia==2 or dia==3 or dia==4 or dia==5 or dia ==6 or dia ==7) ):
                self.acceso = 1
                return 1
            else:
                return 0
        else:
            if(self.get_Tipo_Tarjeta() == "Empleado"):
                if((hora >= 0 and hora <= 23.59 and (dia == 1 or dia==2 or dia==3 or dia==4 or dia==5)) or (hora >= 10 and hora <=15 and (dia == 6 or dia == 7) )):
                    self.acceso = 1
                    return 1
                else:
                    return 0

        return 0

    def esPagoValido(self, dia):
        if(self.acceso == 1):
            if(dia == 5):
                return 1
            else:
                if((dia == 1 or dia==2 or dia==3 or dia==4) and self.saldo > 0.25):
                    self.saldo = self.saldo - 0.25
                    return 1
        return 0






