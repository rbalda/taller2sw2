class Codigo():
    cantDigitos = 7
    codigo=0
    
    def __init__(self, _codigo):
        self.codigo = _codigo
        self.listaCodigo = list(self.codigo)
        
    def esValido(self):
        
        if (len(self.listaCodigo) ==7 and self.codigo.isdigit()):
            return True
        else:
            return False
            
    def esEmpleado (self):
        if (len(self.listaCodigo) ==7 and self.codigo.isdigit() and self.listaCodigo[0] == "0"
            and self.listaCodigo[1]=="0"):
            return True
        return False

    def esEstudiante (self):
        if (len(self.listaCodigo) ==7 and self.codigo.isdigit() and self.listaCodigo[0] != "0"
            and self.listaCodigo[1]!="0"):
            return True
        return False
