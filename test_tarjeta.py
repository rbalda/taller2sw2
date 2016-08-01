import tarjeta
import puerta

empleado_tarjeta = "0054432" 
estudiante_tarjeta = "4654452" 
assert tarjeta.esValida("235") == false
assert tarjeta.esValida("23543267") == false
assert tarjeta.esValida("2354482") == false
assert tarjeta.esValida(empleado_tarjeta) == false
assert tarjeta.esValida(estudiante_tarjeta) == false

assert tarjeta.esEmpleado(estudiante_tarjeta) == false
assert tarjeta.esEmpleado(empleado_tarjeta) == true



assert isAccesoConcedido(tarjeta.esEmpleado(estudiante_tarjeta), 6, 12) == false
assert isAccesoConcedido(tarjeta.esEmpleado(estudiante_tarjeta), 5, 9) == false

assert isAccesoConcedido(tarjeta.esEmpleado(estudiante_tarjeta), 3, 6) == false
assert isAccesoConcedido(tarjeta.esEmpleado(estudiante_tarjeta), 1, 15) == true
assert isAccesoConcedido(tarjeta.esEmpleado(estudiante_tarjeta), 4, 19) == false

assert isAccesoConcedido(tarjeta.esEmpleado(empleado_tarjeta), 3, 6) == true
assert isAccesoConcedido(tarjeta.esEmpleado(empleado_tarjeta), 4, 19) == true
assert isAccesoConcedido(tarjeta.esEmpleado(empleado_tarjeta), 6, 12) == true
assert isAccesoConcedido(tarjeta.esEmpleado(empleado_tarjeta), 1, 15) == true
