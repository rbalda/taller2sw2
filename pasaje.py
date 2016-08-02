def cancelado(dia, saldo):
    if dia < 0 and dia > 4:
        return 0
    if saldo < 0:
        return 0

    if dia != 4:
        if (saldo - 0.25) >= 0:
            return 1
        return 0

    return 1
