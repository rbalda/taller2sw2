import codigo
import verificaAccesso
import pasajeCobrado
from datetime import datetime, date, time, timedelta
import calendar


x = input("codigo: ")

y=codigo.Codigo (x)

if y.esValido():
    print("es valido")
else:
    print("no es valido")

if y.esEstudiante():
    print("es estu")
else:
    print("no es estu")

if y.esEmpleado():
    print("es emplea")
else:
    print("no es emplea")
    
if verificaAccesso.tieneAcceso (x, datetime.now()):
    print ("acceso concedido")
else:
    print ("acceso denegado")


if (pasajeCobrado.pasajeCobrado("VVV", x, 0.25, datetime.now())==1):
    print ("cobrado")
else:
    print ("no cobrado")
    

if (pasajeCobrado.pasajeCobrado("VVV", x, 0.20, datetime.now())==1):
    print ("cobrado")
else:
    print ("no cobrado")


if (pasajeCobrado.pasajeCobrado("VVV", x, 5, datetime.now())==1):
    print ("cobrado")
else:
    print ("no cobrado")
    
