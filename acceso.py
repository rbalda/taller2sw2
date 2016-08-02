from datetime import datetime
from tarjeta import Tarjeta

def validarTarjeta(tarjeta):
    codigo = tarjeta.codigo
    
    #Tarjeta invalida
    if len(codigo) != 7 or not codigo.isdigit():
        return -1

    #Tarjeta valida
    header = codigo[0:2]
    if "00" in header:
        return 0
    else:
        return 1

def acceso(tarjeta, date, dia):
    lim_inf_est = datetime.strptime("08:00:00", "%H:%M:%S")
    lim_sup_est = datetime.strptime("18:00:00", "%H:%M:%S")
    lim_inf_emp = datetime.strptime("10:00:00", "%H:%M:%S")
    lim_sup_emp = datetime.strptime("15:00:00", "%H:%M:%S")
    new_date = datetime.strptime(date, "%H:%M:%S")

    if dia not in range(1, 8) or validarTarjeta(tarjeta) == -1:
        return 0

    if validarTarjeta(tarjeta) == 0:
        if dia in range(0, 6):
            return 1
        else:
            if new_date > lim_inf_emp and new_date < lim_sup_emp:
                return 1
            else:
                return 0
    if validarTarjeta(tarjeta) == 1:
        if dia in range(0, 6):
            if new_date > lim_inf_est and new_date < lim_sup_est:
                return 1
            else:
                return 0
        else:
            return 0

def pagoExpreso(tarjeta, dia):
    if dia in range(1, 6) and validarTarjeta(tarjeta) != -1:
        return 1
    else:
        return 0

