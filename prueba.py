import unittest
from main import validaracceso


class AddTest(unittest.TestCase):

   def setUp(self):

      pass
   def tearDown(self):
      pass
   def test_codigo_estudiante_true(self):
       self.assertEqual(validaracceso(800,1,1),1)
   def test_codigo_estudiante_false(self):
       self.assertEqual(validaracceso(700,1,1),1)
   def test_codigo_empleado_false(self):
       self.assertEqual(validaracceso(700,6,0),1)
if __name__=='__main__':
   unittest.main()
