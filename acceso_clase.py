class Acceso():


    def verificar_id(identificacion):
        numero = str(identificacion)
        esEmpleado = 0
        if (numero[0] == "0" and numero[1] == "0"):
            esEmpleado = 1
        return esEmpleado




    def permiso(id,hora,dia):
        if(id == 0):
            if(dia == 6 or dia == 7):
                if(hora>=10 and hora<=15):
                    return 1
                else:
                    return 0
            else:
                return 1


        else:
            if(dia>=1 and dia <=5):
                if(hora>=8 and hora<=18):
                    return 1
                else:
                    return 0
            else:
                return 0

    def pago(id,dia,saldo):
        if(dia >= 1 and dia <= 4):
            if(saldo<0.25):
                return 0
            else:
                return 1
        else:
            if(dia == 5):
                return 1
            else
                return 0