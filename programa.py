import codigo
import verificaAccesso


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
    
if verificaAccesso.tieneAcceso (x):
    print ("acceso concedido")
else:
    print ("acceso denegado")
    
