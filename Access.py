
from Tarjeta import Tarjeta

class Access():
    """
    Autor: Branny Chito
    Nombre de funci : getAccess
    Entrada: string con el codigo de identificacion, dia, hora en enteros
    Salida: 00 o 01 si es o no valido el Acceso
    """
    def getAccess(self, strCard, day, hour):
        resp = '00' #denied access
        card = Tarjeta();

        # card is valid?
        if card.isValid(strCard) == True:
            if hour>=0 and hour<=24 and day>=1 and day<=7:
                # student
                if strCard[0:2] > '00' and hour>=8 and hour<=18 and day>=1 and day<=5:
                    resp = '01'

                # employed
                if strCard[0:2] == '00':
                    if day<=5:
                        resp = '01'
                    else:
                        if hour>=10 and hour<=15:
                            resp = '01'
        return resp
