from django.test import TestCase
import unittest

# Create your tests herefdsfdsfdsf.
#creando nueva pruebita
'''
from ingreso_pacientes.models import Paciente


class CrearPaciente(TestCase):

def crear_paciente(self):
    self.paciente = Paciente.objects.create(nombres='Juan',apellidos='Vargas',cedula='0955555555')

def test_crear_paciente(self):
    self.crear_paciente()
    self.assertIsInstance(self.paciente,Paciente,'paciente creado exitosamente')
'''
from acceso_clase import Acceso


class ProbarSistemaAcceso(unittest.TestCase):

def test_escenario1(self):

    acceso_edi = Acceso()
    identi = acceso_edi.verificar_id(identificacion=0012345)
    resultado = acceso_edi.permiso(id=identi, hora=10, dia=2)
    self.assertEqual(resultado,1)

def test_escenario2(self):

    acceso_edi = Acceso()
    identi = acceso_edi.verificar_id(identificacion=1234567)
    resultado = acceso_edi.permiso(id=identi, hora=10, dia=2)
    self.assertEqual(resultado,1)

def test_escenario3(self):

    acceso_edi = Acceso()
    identi = acceso_edi.verificar_id(identificacion=0012345)
    resultado = acceso_edi.permiso(id=identi, hora=18, dia=6)
    self.assertEqual(resultado,0)
                     
def test_escenario4(self):

    acceso_edi = Acceso()
    identi = acceso_edi.verificar_id(identificacion=1234567)
    resultado = acceso_edi.permiso(id=identi, hora=5, dia=2)
    self.assertEqual(resultado,0)

def test_escenario5(self):

    acceso_edi = Acceso()
    identi = acceso_edi.verificar_id(identificacion=1234567)
    resultado = acceso_edi.permiso(id=identi, hora=5, dia=7)
    self.assertEqual(resultado,0)

'''
Pruebas de actividad 2, módulo 3
'''

def test_escenario6(self):

    acceso_edi = Acceso()
    identi = acceso_edi.verificar_id(identificacion=1234567)
    resultado = acceso_edi.pago(id=identi, dia=2, saldo=7.00)
    self.assertEqual(resultado,1)

def test_escenario7(self):

    acceso_edi = Acceso()
    identi = acceso_edi.verificar_id(identificacion=1234567)
    resultado = acceso_edi.pago(id=identi, dia=3, saldo=0.00)
    self.assertEqual(resultado,0)

def test_escenario8(self):

    acceso_edi = Acceso()
    identi = acceso_edi.verificar_id(identificacion=1234567)
    resultado = acceso_edi.pago(id=identi, dia=5, saldo=3.00)
    self.assertEqual(resultado,1)


def test_escenario9(self):

    acceso_edi = Acceso()
    identi = acceso_edi.verificar_id(identificacion=0034567)
    resultado = acceso_edi.permiso(id=identi, dia=3, saldo=5.00)
    self.assertEqual(resultado,1)        

def test_escenario10(self):

    acceso_edi = Acceso()
    identi = acceso_edi.verificar_id(identificacion=0034567)
    resultado = acceso_edi.permiso(id=identi, dia=4, saldo=0.20)
    self.assertEqual(resultado,0)     

def test_escenario11(self):

    acceso_edi = Acceso()
    identi = acceso_edi.verificar_id(identificacion=0034567)
    resultado = acceso_edi.permiso(id=identi, dia=5, saldo=3.00)
    self.assertEqual(resultado,1)     

def test_escenario12(self):

    acceso_edi = Acceso()
    identi = acceso_edi.verificar_id(identificacion=1234567)
    resultado = acceso_edi.pago(id=identi, dia=7, saldo=3.00)
    self.assertEqual(resultado,1)

def test_escenario13(self):

    acceso_edi = Acceso()
    identi = acceso_edi.verificar_id(identificacion=0034567)
    resultado = acceso_edi.permiso(id=identi, dia=10, saldo=3.00)
    self.assertEqual(resultado,1)     
