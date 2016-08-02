from django.test import TestCase
import unittest

# Create your tests herefdsfdsfdsf.
#creando nueva pruebita
'''
respuesta(self,idTarjeta,edad,altura,genero):
def respuesta(self,tipoUsuario,dia,hora):


'''
from validorTarjetas import Validador
from resultadoPuerta import Puerta


class ProbarSistemaPuerta(unittest.TestCase):

    def test_escenario1(self):
        validar = Validador()
        tipoUsu = validar.respuesta('23213',18,101,0)
        puerta = Puerta()
        resp = puerta.respuesta(tipoUsu,1,'00h00')
        self.assertEqual(resp,1)

    def test_escenario2(self):
        validar = Validador()
        tipoUsu = validar.respuesta('0012345',18,101,0)
        puerta = Puerta()
        resp = puerta.respuesta(tipoUsu,1,'08h00')
        self.assertEqual(resp,1)

    def test_escenario3(self):
        validar = Validador()
        tipoUsu = validar.respuesta('0012345',18,101,0)
        puerta = Puerta()
        resp = puerta.respuesta(tipoUsu,7,'08h00')
        self.assertEqual(resp,0)

    def test_escenario4(self):
        validar = Validador()
        tipoUsu = validar.respuesta('0012345',18,100,0)
        puerta = Puerta()
        resp = puerta.respuesta(tipoUsu,1,'08h00')
        self.assertEqual(resp,0)

    def test_escenario5(self):
        validar = Validador()
        tipoUsu = validar.respuesta('8912345',18,101,0)
        puerta = Puerta()
        resp = puerta.respuesta(tipoUsu,1,'08h00')
        self.assertEqual(resp,1)

    def test_escenario6(self):
        validar = Validador()
        tipoUsu = validar.respuesta('8912345',18,101,0)
        puerta = Puerta()
        resp = puerta.respuesta(tipoUsu,6,'08h00')
        self.assertEqual(resp,0)

    def test_escenario7(self):
        validar = Validador()
        tipoUsu = validar.respuesta('8912345',18,101,0)
        puerta = Puerta()
        resp = puerta.respuesta(tipoUsu,6,'13h00')
        self.assertEqual(resp,1)

    def test_escenario8(self):
        validar = Validador()
        tipoUsu = validar.respuesta('8912345',18,101,0)
        puerta = Puerta()
        resp = puerta.respuesta(tipoUsu,4,'134300')
        self.assertEqual(resp,0)

    def test_escenario9(self):
        validar = Validador()
        tipoUsu = validar.respuesta('8912345',168,101,0)
        puerta = Puerta()
        resp = puerta.respuesta(tipoUsu,4,'13h00')
        self.assertEqual(resp,0)

    def test_escenario10(self):
        validar = Validador()
        tipoUsu = validar.respuesta('8912345',18,181,2)
        puerta = Puerta()
        resp = puerta.respuesta(tipoUsu,4,'13h00')
        self.assertEqual(resp,0)

    def test_escenario11(self):
        validar = Validador()
        tipoUsu = validar.respuesta('0012345',158,181,0)
        puerta = Puerta()
        resp = puerta.respuesta(tipoUsu,3,'09h00')
        self.assertEqual(resp,0)

    def test_escenario12(self):
        validar = Validador()
        tipoUsu = validar.respuesta('0012345',18,181,5)
        puerta = Puerta()
        resp = puerta.respuesta(tipoUsu,5,'10h00')
        self.assertEqual(resp,0)

    
    
