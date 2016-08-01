def main():
    cod = str(input("codigo:"))
    fecha = str(input("fecha:"))
    hora= str(input("hora:"))
    n=acceso(cod)
    validaracceso(hora,fecha,n)

def acceso(codigo):
    if(len(codigo)<=7 & len(codigo)>5):
        return 1
    elif (len(codigo)<=5):
        return 0
    else:
        return 2

def validaracceso(hora,fecha,n):
    if n==1:
        if (fecha<=5):
            if (hora>=800 & hora <=1800):
                print("ACCESO ESTUDIANTE CONCEDIDO")
                return 1
            else:
                print("ACCESO NO CONCEDIDO")
                return 0
        else:
            print("ACCESO NO CONCEDIDO")
            return 0
    elif n==0:
        print("ACCESO EMPLEADO CONCEDIDO")
        return 1
