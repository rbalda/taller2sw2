import codigo
from datetime import datetime, date, time, timedelta
import calendar

def tieneAcceso (cod):
    c = codigo.Codigo (cod)
    hoy = datetime.now()
    horaActual = time (hoy.hour, hoy.minute, hoy.second)
    print("\tHoraActual:", horaActual)
    
    horaEstudianteInicio = time(8, 0, 0)  # Asigna 8h 0m 0s
    horaEstudianteFin = time(18, 0, 0)  # Asigna 18h 0m 0s
    print("\tHora1:", horaEstudianteInicio)
    print("\tHora1:", horaEstudianteFin)
    horaEmpleadoInicio = time(10, 0, 0)  # Asigna 10h 0m 0s
    horaEmpleadoFin = time(15, 0, 0)  # Asigna 15h 0m 0s
    print("\tHora2:", horaEmpleadoInicio)
    print("\tHora2:", horaEmpleadoFin)
    
    if (datetime.isoweekday(hoy) >0 and datetime.isoweekday(hoy)<6):
        if c.esEstudiante and horaEstudianteInicio<= horaActual and horaEstudianteFin>=horaActual:
            return 1
        if c.esEmpleado:
            return 1
    else:
        if c.esEmpleado and horaEmpleadoInicio <=horaActual and horaEmpleadoFin<=horaActual:
            return 1
        return 0
    return 0
            
