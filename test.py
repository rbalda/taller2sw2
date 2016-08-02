import unittest
from Tarjeta import Tarjeta

class TestTarjeta(unittest.TestCase):


    def test_codigo_invalido(self):
        t = Tarjeta()
        acceso = t.validar_tarjetas("TRABAJADOR", "00210", "10H00", "MARTES")
        self.assertEqual(t.abrir_puerta(acceso), 0)

    def test_codigo_valido_trabajador(self):
        #DIA LABORAL
        t = Tarjeta()
        acceso = t.validar_tarjetas("TRABAJADOR", "0021015", "10H00", "MIERCOLES")
        self.assertEqual(t.abrir_puerta(acceso), 1)

    def test_codigo_valido_trabajador2(self):
        #FIN DE SEMANA
        t = Tarjeta()
        acceso = t.validar_tarjetas("TRABAJADOR", "0021015", "11H00", "SABADO")
        self.assertEqual(t.abrir_puerta(acceso), 1)

    def test_codigo_invalido_trabajador3(self):
        #FIN DE SEMANA HORA INVALIDA
        t = Tarjeta()
        acceso = t.validar_tarjetas("TRABAJADOR", "0021015", "16H00", "DOMINGO")
        self.assertEqual(t.abrir_puerta(acceso), 0)

    def test_codigo_invalido_trabajador4(self):
        #CODIGO INVALIDO
        t = Tarjeta()
        acceso = t.validar_tarjetas("TRABAJADOR","3021015","16H00","LUNES")
        self.assertEqual(t.abrir_puerta(acceso), 0)

    def test_codigo_valido_estudiante(self):
        #DIA LABORAL
        t = Tarjeta()
        acceso = t.validar_tarjetas("ESTUDIANTE", "1221015", "16H00", "LUNES")
        self.assertEqual(t.abrir_puerta(acceso), 1)

    def test_codigo_invalido_estudiante2(self):
        #DIA LABORAL HORA INVALIDA
        t = Tarjeta()
        acceso = t.validar_tarjetas("ESTUDIANTE", "1221015", "20H00", "MIERCOLES")
        self.assertEqual(t.abrir_puerta(acceso),0)

    def test_codigo_invalido_estudiante3(self):
        #DIA LABORAL DIA INVALIDA
        t = Tarjeta()
        acceso = t.validar_tarjetas("ESTUDIANTE", "1221015", "10H00", "SABADO")
        self.assertEqual(t.abrir_puerta(acceso),0)

    def test_codigo_invalido_estudiante4(self):
        #CODIGO INVALIDO
        t = Tarjeta()
        acceso = t.validar_tarjetas("ESTUDIANTE", "0021015", "11H00", "MIERCOLES")
        self.assertEqual(t.abrir_puerta(acceso),0)

    def test_pasajeTrabajador_valido(self):
        t = Tarjeta()
        acceso = t.validar_tarjetas("TRABAJADOR", "0021015", "10H00", "MIERCOLES")
        puerta= t.abrir_puerta(acceso)
        self.assertEqual(t.pago_pasaje(puerta,"MIERCOLES",10.00), 1)

    def test_pasajeTrabajador_valido2(self):
        #VIERNES
        t = Tarjeta()
        acceso = t.validar_tarjetas("TRABAJADOR", "0096015", "12H00", "VIERNES")
        puerta= t.abrir_puerta(acceso)
        print(puerta)
        print(t.pago_pasaje(puerta,"VIERNES",4.00))
        self.assertEqual(t.pago_pasaje(puerta,"VIERNES",4.00), 1)

    def test_pasajeTrabajador_invalido(self):
        #saldo es negativo
        t = Tarjeta()
        acceso = t.validar_tarjetas("TRABAJADOR", "0021015", "11H00", "LUNES")
        puerta= t.abrir_puerta(acceso)
        self.assertEqual(t.pago_pasaje(puerta,"LUNES",0.00), 0)

    def test_pasajeEstudiante_valido(self):
        t = Tarjeta()
        acceso = t.validar_tarjetas("ESTUDIANTE", "4721015", "16H00", "MIERCOLES")
        puerta= t.abrir_puerta(acceso)
        self.assertEqual(t.pago_pasaje(puerta,"MIERCOLES",2.00), 1)

    def test_pasajeEstudiante_valido2(self):
        #VIERNES
        t = Tarjeta()
        acceso = t.validar_tarjetas("ESTUDIANTE", "4721015", "15H00", "VIERNES")
        puerta= t.abrir_puerta(acceso)
        print(puerta)
        self.assertEqual(t.pago_pasaje(puerta,"VIERNES",3.00), 1)

    def test_pasajeEstudiante_invalido(self):
        #saldo es negativo
        t = Tarjeta()
        acceso = t.validar_tarjetas("ESTUDIANTE", "6921015", "13H00", "LUNES")
        puerta= t.abrir_puerta(acceso)
        self.assertEqual(t.pago_pasaje(puerta,"LUNES",0.20), 0)

if __name__ == '__main__':
    unittest.main()
