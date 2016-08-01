def isAccesoConcedido(esEmpleado, dia, hora):
    if dia > 6 or dia < 0 :
        return 0
    if hora > 23 or hora < 0 :
        return 0

    if esEmpleado:
        if dia < 5:
            return 1
        elif hora > 10 and hora < 15:
	    return 1
    else:
        if dia < 5 and hora > 8 and hora < 18:
	    return 1

    return 0
	    
