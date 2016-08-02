import codigo
from datetime import datetime, date, time, timedelta
import calendar

def tieneAcceso (cod, fechaHora):
    c = codigo.Codigo (cod)
    #hoy = datetime.now()
    hoy = fechaHora
    horaActual = time (hoy.hour, hoy.minute, hoy.second)
    print("\tHoraActual:", horaActual)
    
    horaEstudianteInicio = time(8, 0, 0)  # Asigna 8h 0m 0s
    horaEstudianteFin = time(18, 0, 0)  # Asigna 18h 0m 0s
    horaEmpleadoInicio = time(10, 0, 0)  # Asigna 10h 0m 0s
    horaEmpleadoFin = time(15, 0, 0)  # Asigna 15h 0m 0s
    
    if (datetime.isoweekday(hoy) >0 and datetime.isoweekday(hoy)<6):
        if c.esEstudiante() and horaEstudianteInicio<= horaActual and horaEstudianteFin>=horaActual:
            print("\tEs estudiante. Acceso concedido. Dia entresemana")
            return 1
        if c.esEmpleado():
            print("\tEs empleadlo. Acceso concedido. Dia entresemana")
            return 1
    else:
        if c.esEmpleado() and horaEmpleadoInicio <=horaActual and horaEmpleadoFin>=horaActual:
            print("\tEs empleado. Acceso concedido. Fin de semana")
            return 1
        return 0
    return 0
            
