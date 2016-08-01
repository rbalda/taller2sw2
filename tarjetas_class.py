
class Tarjeta():

    def get_Tipo_Tarjeta(self, numero):
        if(numero.isdigit()): # Only digit in this string
            if(len(numero) == 7):
                if(numero[0] == '0' and numero [1] == '0'):
                    return "Empleado"
                else:
                    return "Estudiante"
        return "Invalido"

    def esHorarioValido(self, numeroT, dia, hora):
        if(self.get_Tipo_Tarjeta(numeroT) == "Estudiante"):
            if(hora >= 8 and hora <= 18 and (dia == 1 or dia==2 or dia==3 or dia==4 or dia==5 or dia ==6 or dia ==7) ):
                return 1
            else:
                return 0
        else:
            if(self.get_Tipo_Tarjeta(numeroT) == "Empleado"):
                if((hora >= 0 and hora <= 23.59 and (dia == 1 or dia==2 or dia==3 or dia==4 or dia==5)) or (hora >= 10 and hora <=15 and (dia == 6 or dia == 7) )):
                    return 1
                else:
                    return 0

        return 0


