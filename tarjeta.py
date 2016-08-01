def esValida(codigo):
    return len(codigo) == 7

def esEmpleado(codigo):
    if not esValida(codigo):
        raise Exception "La tarjeta no es valida!"
    return codigo.startsWith("00")
    
