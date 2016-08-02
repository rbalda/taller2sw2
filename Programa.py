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

    #Modulo 3
    #Sistema de pagos
    #En esta función tarjeta va a ser un array que contiene [Código, Nombres y apellidos, Saldo]
    def modulo_3_sistema_pagos(self, tarjeta, dia):
        if(len(tarjeta) == 3):
            codigo_tarjeta_valida = Programa.modulo_1_verificar_tarjeta(tarjeta[0])
            if(codigo_tarjeta_valida[0]):
                if(Programa.validar_dia_expreso(dia)):
                    if(dia>=1 and dia <=4):
                        if(Programa.saldo_disponible_valido(tarjeta[2])):
                            tarjeta[2] -= 0.25
                            return "Pasaje cobrado exitosamente"
                    else:
                        return "Pasaje cobrado exitosamente"
        return "No se pudo cobrar el pasaje"
    #Verifica si el saldo disponible en la tarjeta es válido
    def saldo_disponible_valido(saldo):
        if(isinstance( saldo, int ) or isinstance( saldo, float )):
            if(saldo >= 0.25):
                return True
        return False
    #Verifica si el día de expreso es válido
    def validar_dia_expreso(dia):
        if(isinstance( dia, int )):
            if(dia >= 1 and dia <= 5):
                return True
        return False
