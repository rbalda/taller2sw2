import codigo
from datetime import datetime, date, time, timedelta
import calendar


def pasajeCobrado (nombreCompleto, cod, saldo, fechaHora):
    c = codigo.Codigo(cod)
    hoy = fechaHora
    cobroExitoso = 0

    if c.esValido():
        print ("Codigo valido")
        if (datetime.isoweekday(hoy)==5):
            print ("es viernes y es GRATIS!")
            cobroExitoso=1
        elif (datetime.isoweekday(hoy) >0 and datetime.isoweekday(hoy)<5):
            print ("de lunes a jueves")
            if (saldo >= 0.25):
                saldo=saldo-0.25
                print ("saldo actual: "+str(saldo))
                cobroExitoso=1
            else:
                print ("saldo insuficiente: "+ str(saldo))
                cobroExitoso=0
    else:
        print ("Codigo invalido")
        cobroExitoso = 0

    
    
    return cobroExitoso
