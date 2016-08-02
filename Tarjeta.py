class Tarjeta():
    """
    Autor: Branny Chito
    Nombre de funci : isValid
    Entrada: string con el codigo de identificacion
    Salida: tru o false si es o no valido el codigo
    """
    def isValid(self, strId):
        resp = False;
        if len(strId) == 7 and strId[0:2]>='00' and strId[0:2]<='99':
            resp = True;
        return resp;
    
