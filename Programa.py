#Autor: Johnny Suárez
class Programa():

    #Verificación si se premite el acceso
    def verificar_acceso(self,tarjeta,dia,hora):
        tarjeta_valida = Programa.modulo_1_verificar_tarjeta(tarjeta)
        if(tarjeta_valida[0]):
            if(Programa.modulo_2_acceso_valido(tarjeta_valida[1],dia,hora)):
                return("Acceso Concedido")
            else:
                return ("Acceso Denegado")
        else:
            return("Acceso Denegado")

    #Módulo 1
    #Verifica si la tarjeta es válida además de identificar el tipo de persona al que pertenece
    def modulo_1_verificar_tarjeta(tarjeta):
        numero_valido = Programa.numero_tarjeta_es_valida(tarjeta)
        tipo_persona = ""
        if(numero_valido):
            tipo_persona = Programa.identificar_tipo_persona(tarjeta)
        return [numero_valido, tipo_persona]
    #Verificar si el numero de la tarjeta es válida(Entero, Longitud)
    def numero_tarjeta_es_valida(tarjeta):
        condiciones = 0
        if(tarjeta.isdigit()):
            condiciones += 1
        if(len(tarjeta) == 7):
            condiciones +=1
        if(condiciones == 2):
            return True
        return False
    #Identificación del tipo de persona
    def identificar_tipo_persona(tarjeta):
        if(tarjeta[0:2] == "00"):
            return "Empleado"
        return "Estudiante"

    #Módulo 2
    #Verificar si el acceso pedido es válido
    def modulo_2_acceso_valido(tipo_persona, dia, hora):
        dia_valido = Programa.validar_dia(dia)
        hora_valida = Programa.validar_hora(hora)
        if(dia_valido and hora_valida):
            if(Programa.validar_dia_hora_tipo_persona(tipo_persona,dia,hora)):
                return True
        return False
    #Verifica si el día es válido(Entero, Entre 1-7)
    def validar_dia(dia):
        if(isinstance( dia, int )):
            if(dia >= 1 and dia <= 7):
                return True
        return False
    #Verifica si la hora es válida(Entero, Entre 0-23)
    def validar_hora(hora):
        if(isinstance( hora, int )):
            if(hora >= 0 and hora <= 23):
                return True
        return False
    #Verifica si el acceso es permitido dependiendo del tipo de persona y el horario
    def validar_dia_hora_tipo_persona(tipo_persona,dia,hora):
        if(tipo_persona == "Empleado"):
            if(dia>=1 and dia<=5):
                return True
            if(dia>=6 and dia<=7):
                if(hora>=10 and hora<=15):
                    return True
        if(dia>=1 and dia<=5):
            if(hora>=8 and hora<=18):
                return True
        return False
