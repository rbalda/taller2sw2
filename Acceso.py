
class Acceso:

    def getAcceso(self,tipo,dia, hora):

        if(type(dia)!= int or type(hora)!= int):
            return 0
        if(tipo == ""):
            return 0
        elif(tipo == "Estudiante"):
            if(dia == 5 or dia == 6):
                return 0
            else:
                if(hora>=8 and hora<=18 ):
                    return 1
                else:
                    return 0
        else:
            if(dia == 5 or dia == 6):
                if(hora>=10 and hora<=15 ):
                    return 1
                else:
                    return 0
            else:
                return 1