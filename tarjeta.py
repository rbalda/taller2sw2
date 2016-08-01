def esValida(codigo):
    return len(codigo) == 7

def esEmpleado(codigo):
    if not esValida(codigo):
        raise ValueError("La tarjeta no es valida!")
    return codigo.startswith("00")
    
