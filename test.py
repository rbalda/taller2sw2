import unittest
from accesoFiec import acceso


class AddTest(unittest.TestCase):

   def setUp(self):
      pass
   def tearDown(self):
      pass
   def test_estudiante_diasLaborables(self):
       self.assertEqual(acceso('1234567',3,'12H00'),1)
   def test_estudiante_diasNoLaborables(self):
       self.assertEqual(acceso('1234567',6,'12H00'),0)
   def test_estudiante_horaMenor10(self):
       self.assertEqual(acceso('1234567',2,'09H00'),0)
   def test_estudiante_horaMayor18(self):
       self.assertEqual(acceso('1234567',2,'19H00'),0)
   def test_estudiante_horaPermitida(self):
       self.assertEqual(acceso('1234567',2,'13H00'),1)
   def test_empleado_diaSemana24Horas(self):
       self.assertEqual(acceso('0012345',2,'15H00'),1)
   def test_empleado_finDeSemanaHoraMenor10(self):
       self.assertEqual(acceso('0012345',6,'08H00'),0)
   def test_empleado_finDeSemanaHoraMayor15(self):
       self.assertEqual(acceso('0012345',6,'16H00'),0)
   def test_empleado_finDeSemanaHoraPermitida(self):
       self.assertEqual(acceso('0012345',6,'13H00'),1)

if __name__=='__main__':
    unittest.main()
