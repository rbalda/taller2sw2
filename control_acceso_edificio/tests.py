import unittest


'''
respuesta(self,idTarjeta,edad,altura,genero):
def respuesta(self,tipoUsuario,dia,hora):
def respuesta(self,apellido,nombre,idTarjeta,saldo,dia):

'''
from validorTarjetas import Validador
from resultadoPuerta import Puerta
from pagoExpreso import sistemaPago


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

'''Pruebas para el modulo 3 de pasajes'''

    def test_escenario13(self):
        sistCobro = sistemaPago()
        resp = sistCobro.respuesta('Ayala','Jorge','0012345',0.50,1)
        self.assertEqual(resp,1)

    def test_escenario14(self):
        sistCobro = sistemaPago()
        resp = sistCobro.respuesta('Ayala','Jorge','4512345',0.50,4)
        self.assertEqual(resp,1)

    def test_escenario15(self):
        sistCobro = sistemaPago()
        resp = sistCobro.respuesta('Ayala','Jorge','4512345',0.50,5)
        self.assertEqual(resp,1)

    def test_escenario16(self):
        sistCobro = sistemaPago()
        resp = sistCobro.respuesta('Ayala','Jorge','0012345',0.50,5)
        self.assertEqual(resp,1)

    def test_escenario17(self):
        sistCobro = sistemaPago()
        resp = sistCobro.respuesta('Ayala','Jorge','0012345',0.50,6)
        self.assertEqual(resp,0)

    def test_escenario18(self):
        sistCobro = sistemaPago()
        resp = sistCobro.respuesta('Ayala','Jorge','4512345',0.50,7)
        self.assertEqual(resp,0)

    def test_escenario19(self):
        sistCobro = sistemaPago()
        resp = sistCobro.respuesta('Ayala','Jorge','0012345',0.05,1)
        self.assertEqual(resp,0)

    def test_escenario20(self):
        sistCobro = sistemaPago()
        resp = sistCobro.respuesta('Ayala','Jorge','4512345',0.05,4)
        self.assertEqual(resp,0)

    def test_escenario21(self):
        sistCobro = sistemaPago()
        resp = sistCobro.respuesta('Ayala','Jorge','2345',0.05,4)
        self.assertEqual(resp,0)


if __name__ == '__main__':
    unittest.main()

    
    
