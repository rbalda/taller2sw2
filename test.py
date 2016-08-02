import unittest
from accesoFiec import acceso,Tarjeta,cobrar

#taller
class AddTest(unittest.TestCase):
   def setUp(self):
       self.tarjeta = Tarjeta('Cristian','2938476',1)

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
   def test_diaGratis_Bus(self):
       self.assertEqual(cobrar(self.tarjeta,5),0)
   def test_diaCobrado_Bus(self):
       self.assertEqual(cobrar(self.tarjeta,3),1)
   def test_diaFinDeSemana_Bus(self):
       self.assertEqual(cobrar(self.tarjeta,6),0)
   def test_saldoMayor25ctvs_Bus(self):
       self.assertEqual(cobrar(self.tarjeta,1),1)
   def test_saldoMenor25ctvs_Bus(self):
       self.tarjeta.Saldo=0.15
       self.assertEqual(cobrar(self.tarjeta,1),0)

if __name__=='__main__':
    unittest.main()
