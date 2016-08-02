
class Tarjeta:

     def validarTarjeta(self, codigo):
        self.digitos = ""
        if(type(codigo)!= str):
            return ""
        if(len(codigo) <7):
            return ""
        else:
            self.digitos = codigo[1:2]

        if(self.digitos == "00"):
            return "Empleado"
        else:
            return "Estudiante"
