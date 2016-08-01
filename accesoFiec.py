def validarTarjeta(codigo):
    if(codigo[:2]=='00'): return 1
    else: return 0

def acceso(codigo,dia,hora):
    hora=int(hora[:2])

    tipoUsuario=validarTarjeta(codigo)
    if(tipoUsuario==0 and dia>0 and dia<=5 and hora>=10 and hora<=18):
        return 1
    elif(tipoUsuario==1):
        if(dia>0 and dia<=5):
            return 1
        elif(dia>=6 and dia<=7 and hora>=10 and hora<=15):
            return 1
        else:
            return 0
    else: return 0
