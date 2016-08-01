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
from prestamo_clase import Prestamo


class ProbarSistemaPrestamo(unittest.TestCase):

    def test_escenario1(self):

        acceso_edi = Prestamo()
        identi = acceso_edi.verificar_id(identificacion=0012345)
        resultado = acceso_edi.permiso(id=identi, hora=10, dia=2)
        self.assertEqual(resultado,1)

    def test_escenario2(self):

        acceso_edi = Prestamo()
        identi = acceso_edi.verificar_id(identificacion=1234567)
        resultado = acceso_edi.permiso(id=identi, hora=10, dia=2)
        self.assertEqual(resultado,1)

    def test_escenario3(self):

        acceso_edi = Prestamo()
        identi = acceso_edi.verificar_id(identificacion=0012345)
        resultado = acceso_edi.permiso(id=identi, hora=18, dia=6)
        self.assertEqual(resultado,0)
                         
    def test_escenario4(self):

        acceso_edi = Prestamo()
        identi = acceso_edi.verificar_id(identificacion=1234567)
        resultado = acceso_edi.permiso(id=identi, hora=5, dia=2)
        self.assertEqual(resultado,0)

    def test_escenario5(self):

        acceso_edi = Prestamo()
        identi = acceso_edi.verificar_id(identificacion=1234567)
        resultado = acceso_edi.permiso(id=identi, hora=5, dia=7)
        self.assertEqual(resultado,0)

        
