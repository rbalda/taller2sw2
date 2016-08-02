import tarjeta
import puerta
import pasaje

def test_sistema():
    empleado_tarjeta = "0054432" 
    estudiante_tarjeta = "4654452" 
    assert tarjeta.esValida("235") == False
    assert tarjeta.esValida("23543267") == False
    assert tarjeta.esValida("2354482") == True
    assert tarjeta.esValida(empleado_tarjeta) == True
    assert tarjeta.esValida(estudiante_tarjeta) == True

    assert tarjeta.esEmpleado(estudiante_tarjeta) == False
    assert tarjeta.esEmpleado(empleado_tarjeta) == True



    assert puerta.isAccesoConcedido(tarjeta.esEmpleado(estudiante_tarjeta), 6, 12) == False
    assert puerta.isAccesoConcedido(tarjeta.esEmpleado(estudiante_tarjeta), 5, 9) == False

    assert puerta.isAccesoConcedido(tarjeta.esEmpleado(estudiante_tarjeta), 3, 6) == False
    assert puerta.isAccesoConcedido(tarjeta.esEmpleado(estudiante_tarjeta), 1, 15) == True
    assert puerta.isAccesoConcedido(tarjeta.esEmpleado(estudiante_tarjeta), 4, 19) == False

    assert puerta.isAccesoConcedido(tarjeta.esEmpleado(empleado_tarjeta), 3, 6) == True
    assert puerta.isAccesoConcedido(tarjeta.esEmpleado(empleado_tarjeta), 4, 19) == True
    assert puerta.isAccesoConcedido(tarjeta.esEmpleado(empleado_tarjeta), 6, 12) == True
    assert puerta.isAccesoConcedido(tarjeta.esEmpleado(empleado_tarjeta), 1, 15) == True

def test_horarios_invalidos():
    assert puerta.isAccesoConcedido(tarjeta.esEmpleado("0034567"), 9, 6) == False
    assert puerta.isAccesoConcedido(tarjeta.esEmpleado("0034567"), 2, 55) == False
    
def test_exceptions():
    try:
        raisedException = False
        tarjeta.esEmpleado("534")

    except ValueError:
        raisedException = True
    assert raisedException

def test_pasaje(): 
    assert pasaje.cancelado(0,0.0) == 0
    assert pasaje.cancelado(0,-0.50) == 0
    assert pasaje.cancelado(7,0.50) == 0
    assert pasaje.cancelado(4,0.25) == 1
    assert pasaje.cancelado(2,0.10) == 0
    assert pasaje.cancelado(2,1.00) == 1

test_sistema()
test_horarios_invalidos()
test_exceptions()
test_pasaje()
test_pasaje()
