"""
Autor: Fernando Campaña
Nombre de funcin: validar_tarjeta
Entrada: codigo de acceso de la tarjeta
Salida: string con el tipo de permiso
Descripcion: Funcion que valida una tarjeta.
"""
def validar_tarjeta(codigo_acceso):
	if(codigo_acceso >= 0 and codigo_acceso <= 99999):
		return "empleado"
	elif(codigo_acceso > 99999 and codigo_acceso <= 9999999):
		return "estudiante"
	else:
		return "invalido"
