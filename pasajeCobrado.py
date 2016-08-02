import codigo
from datetime import datetime, date, time, timedelta
import calendar
import tarjeta


def pasajeCobrado (nombreCompleto, cod, saldo, fechaHora):
    c = codigo.Codigo(cod)
    hoy = fechaHora
    cobroExitoso = 0
    pasaje=0.25
    
    t = tarjeta.Tarjeta (nombreCompleto, cod, saldo)
    

    if t.esValida():
        print ("tarjeta valido")
        if (datetime.isoweekday(hoy)==5):
            print ("es viernes y es GRATIS!")
            cobroExitoso=1
        elif (datetime.isoweekday(hoy) >0 and datetime.isoweekday(hoy)<5):
            print ("de lunes a jueves")
            if (t.haySaldoDisponible(pasaje)):
                t.debitarSaldo(pasaje)
                print ("saldo actual: "+str(t.saldo))
                cobroExitoso=1
            else:
                print ("saldo insuficiente: "+ str(t.saldo))
                cobroExitoso=0
    else:
        print ("tarjeta invalido")
        cobroExitoso = 0

    
    
    return cobroExitoso
