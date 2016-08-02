import unittest
from Tarjeta import Tarjeta

class TestTarjeta(unittest.TestCase):


    def test_codigo_invalido(self):
        t = Tarjeta("Julio","Aguirre", "00210",5.00)
        acceso = t.validar_tarjetas("TRABAJADOR", t.codigo, "10H00", "MARTES")
        self.assertEqual(t.abrir_puerta(acceso), 0)

    def test_codigo_valido_trabajador(self):
        #DIA LABORAL
        t = Tarjeta("Julio","Aguirre", "0021015",5.00)
        acceso = t.validar_tarjetas("TRABAJADOR", t.codigo, "10H00", "MIERCOLES")
        self.assertEqual(t.abrir_puerta(acceso), 1)

    def test_codigo_valido_trabajador2(self):
        #FIN DE SEMANA
        t = Tarjeta("Julio","Aguirre", "0021015",5.00)
        acceso = t.validar_tarjetas("TRABAJADOR", t.codigo, "11H00", "SABADO")
        self.assertEqual(t.abrir_puerta(acceso), 1)

    def test_codigo_invalido_trabajador3(self):
        #FIN DE SEMANA HORA INVALIDA
        t = Tarjeta("Julio","Aguirre", "0021015",5.00)
        acceso = t.validar_tarjetas("TRABAJADOR", t.codigo, "16H00", "DOMINGO")
        self.assertEqual(t.abrir_puerta(acceso), 0)

    def test_codigo_invalido_trabajador4(self):
        #CODIGO INVALIDO
        t = Tarjeta("Julio","Aguirre", "3021015",5.00)
        acceso = t.validar_tarjetas("TRABAJADOR",t.codigo,"16H00","LUNES")
        self.assertEqual(t.abrir_puerta(acceso), 0)

    def test_codigo_valido_estudiante(self):
        #DIA LABORAL
        t = Tarjeta("Julio","Aguirre", "1221015",5.00)
        acceso = t.validar_tarjetas("ESTUDIANTE", t.codigo, "16H00", "LUNES")
        self.assertEqual(t.abrir_puerta(acceso), 1)

    def test_codigo_invalido_estudiante2(self):
        #DIA LABORAL HORA INVALIDA
        t = Tarjeta("Julio","Aguirre", "1221015",5.00)
        acceso = t.validar_tarjetas("ESTUDIANTE", t.codigo, "20H00", "MIERCOLES")
        self.assertEqual(t.abrir_puerta(acceso),0)

    def test_codigo_invalido_estudiante3(self):
        #DIA LABORAL DIA INVALIDA
        t = Tarjeta("Julio","Aguirre", "1221015",5.00)
        acceso = t.validar_tarjetas("ESTUDIANTE", t.codigo, "10H00", "SABADO")
        self.assertEqual(t.abrir_puerta(acceso),0)

    def test_codigo_invalido_estudiante4(self):
        #CODIGO INVALIDO
        t = Tarjeta("Julio","Aguirre", "0021015",5.00)
        acceso = t.validar_tarjetas("ESTUDIANTE", t.codigo, "11H00", "MIERCOLES")
        self.assertEqual(t.abrir_puerta(acceso),0)

    def test_pasajeTrabajador_valido(self):
        #(self,nombre,apellido,codigo,saldo
        t = Tarjeta("Julio","Aguirre", "0021015",10.00)
        acceso = t.validar_tarjetas("TRABAJADOR",t.codigo, "10H00", "MIERCOLES")
        puerta= t.abrir_puerta(acceso)
        print(t.saldo)
        self.assertEqual(t.pago_pasaje(puerta,"MIERCOLES",t.saldo), 1)

    def test_pasajeTrabajador_valido2(self):
        #VIERNES
        t = Tarjeta("Julio","Aguirre", "0096015",4.00)
        acceso = t.validar_tarjetas("TRABAJADOR", t.codigo, "12H00", "VIERNES")
        puerta= t.abrir_puerta(acceso)
        self.assertEqual(t.pago_pasaje(puerta,"VIERNES",t.saldo), 1)

    def test_pasajeTrabajador_invalido(self):
        #saldo es negativo
        t = Tarjeta("Julio","Aguirre", "0021015",0.00)
        acceso = t.validar_tarjetas("TRABAJADOR", t.codigo, "11H00", "LUNES")
        puerta= t.abrir_puerta(acceso)
        self.assertEqual(t.pago_pasaje(puerta,"LUNES", t.saldo), 0)

    def test_pasajeTrabajador_invalido1(self):
        #FIN DE SEMANA
        t = Tarjeta("Julio","Aguirre", "0021015",5.20)
        acceso = t.validar_tarjetas("TRABAJADOR",t.codigo,"14H00","SABADO")
        puerta= t.abrir_puerta(acceso)
        self.assertEqual(t.pago_pasaje(puerta,"SABADO",t.saldo), 0)

    def test_pasajeTrabajador_invalido2(self):
        #FIN DE SEMANA
        t = Tarjeta("Julio","Aguirre", "1121015",2.20)
        acceso = t.validar_tarjetas("TRABAJADOR",t.codigo,"14H00","DOMINGO")
        puerta= t.abrir_puerta(acceso)
        self.assertEqual(t.pago_pasaje(puerta,"DOMINGO",t.saldo), 0)

    def test_pasajeEstudiante_valido(self):
        t = Tarjeta("Julio","Aguirre", "4721015",2.00)
        acceso = t.validar_tarjetas("ESTUDIANTE", t.codigo, "16H00", "MIERCOLES")
        puerta= t.abrir_puerta(acceso)
        self.assertEqual(t.pago_pasaje(puerta,"MIERCOLES",t.saldo), 1)

    def test_pasajeEstudiante_valido2(self):
        #VIERNES
        t = Tarjeta("Julio","Aguirre", "4721015",3.00)
        acceso = t.validar_tarjetas("ESTUDIANTE", t.codigo, "15H00", "VIERNES")
        puerta= t.abrir_puerta(acceso)
        self.assertEqual(t.pago_pasaje(puerta,"VIERNES",t.saldo), 1)

    def test_pasajeEstudiante_invalido(self):
        #saldo es negativo
        t = Tarjeta("Julio","Aguirre", "6921015",0.20)
        acceso = t.validar_tarjetas("ESTUDIANTE", t.codigo, "13H00", "LUNES")
        puerta= t.abrir_puerta(acceso)
        self.assertEqual(t.pago_pasaje(puerta,"LUNES",t.saldo), 0)



if __name__ == '__main__':
    unittest.main()
