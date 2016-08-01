import unittest
from datetime import datetime, date, time, timedelta

import codigo
import verificaAccesso

class TestAcceso (unittest.TestCase):
    def setUp (self):
        pass

    def tearDown (self):
        pass

    def test_codigoMenosCaracteres (self):
        self.assertEqual(verificaAccesso.tieneAcceso ("123456", datetime(2016, 8, 1, 0, 0, 0)),0)

    def test_codigoMasCaracteres (self):
        self.assertEqual(verificaAccesso.tieneAcceso ("123456789", datetime(2016, 8, 1, 0, 0, 0)),0)

    def test_codigoAlfanumerico (self):
        self.assertEqual(verificaAccesso.tieneAcceso ("A4df33", datetime(2016, 8, 1, 0, 0, 0)),0)

    def test_codigoAlfabetico (self):
        self.assertEqual(verificaAccesso.tieneAcceso ("ABCDEFG", datetime(2016, 8, 1, 0, 0, 0)),0)

    def test_codigoEstudianteFechaHoraOK (self):
        self.assertEqual(verificaAccesso.tieneAcceso ("1234567", datetime(2016, 8, 1, 12, 0, 0)),1)

    def test_codigoEstudianteFechaHoraMayor (self):
        self.assertEqual(verificaAccesso.tieneAcceso ("1234567", datetime(2016, 8, 1, 18, 1, 0)),0)    

    def test_codigoEstudianteFechaHoraMenor (self):
        self.assertEqual(verificaAccesso.tieneAcceso ("1234567", datetime(2016, 8, 1, 7, 59, 0)),0)    

    def test_codigoEstudianteFechaFinde (self):
        self.assertEqual(verificaAccesso.tieneAcceso ("1234567", datetime(2016, 8, 1, 12, 0, 0)),0)    


    def test_codigoEmpleadoFechaOK (self):
        self.assertEqual(verificaAccesso.tieneAcceso ("0034567", datetime(2016, 8, 1, 23, 0, 0)),1)    


    def test_codigoEstudianteFechaFindeOK (self):
        self.assertEqual(verificaAccesso.tieneAcceso ("0034567", datetime(2016, 8, 6, 12, 0, 0)),1)    


    def test_codigoEstudianteFechaFindeMayor (self):
        self.assertEqual(verificaAccesso.tieneAcceso ("0034567", datetime(2016, 8, 6, 9, 59, 0)),0)    

    def test_codigoEstudianteFechaFindeMenor (self):
        self.assertEqual(verificaAccesso.tieneAcceso ("0034567", datetime(2016, 8, 6, 15, 1, 0)),0)    


if __name__=='__main__':
    unittest.main()
