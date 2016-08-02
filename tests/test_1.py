import unittest
from acceso import Acceso
from modulo_tarjeta import Tarjeta
class AccesoTestCase(unittest.TestCase):

    def setUp(self):
        """se la llama antes de cada test"""
        self.tarjeta = Tarjeta("00222223","Estudiante")
        self.acceso = Acceso(self.tarjeta, 1, 25)

    def tearDown(self):
        """llamar luego de cada test"""
        print("termino test")

    def testATiempo(self):
        """test de hora mayor a 24"""
        self.acceso = Acceso(self.tarjeta, 1, 25)
        assert self.acceso.validarHora() == False


    def testBTiempo(self):
        """test de hora menor a 0"""
        self.acceso = Acceso(self.tarjeta, 1, -1)
        assert self.acceso.validarHora() == False


    def testCTiempo(self):
        """test de hora entre 0 y 24"""
        self.acceso = Acceso(self.tarjeta, 1, 18)
        assert self.acceso.validarHora() == True

    def testTarjeta1(self):
        self.tarjeta = Tarjeta("0022222","Estudiante")
        assert self.tarjeta.validarLongitud() == True

    def testTarjeta2(self):
        self.tarjeta = Tarjeta("002222233434","Estudiante")
        assert self.tarjeta.validarLongitud() == False

    def testEstudiante1(self):
        self.tarjeta = Tarjeta("0011221","Estudiante")
        assert self.tarjeta.verificarEstudiante() == True

    def testEstudiante2(self):
        self.tarjeta = Tarjeta("1111221","Estudiante")
        assert self.tarjeta.verificarEstudiante() == False

    def testValidarTipoUsuario1(self):
        self.tarjeta = Tarjeta("1111221","Empleado")
        assert self.tarjeta.validarUsuario() == True

    def testValidarTipoUsuario2(self):
        self.tarjeta = Tarjeta("0011221","Empleado")
        assert self.tarjeta.validarUsuario() == False

    def testValidarTipoUsuario3(self):
        self.tarjeta = Tarjeta("0011221","Estudiante")
        assert self.tarjeta.validarUsuario() == True

    def testValidarDigitos1(self):
        self.tarjeta = Tarjeta("0011222221","Empleado")
        assert self.tarjeta.validarUsuario() == False

    def testValidarDigitos2(self):
        self.tarjeta = Tarjeta("aaaaaas","Empleado")
        assert self.tarjeta.validarUsuario() == False

    def testValidarAcceso1(self):
        self.tarjeta = Tarjeta("00222223","Estudiante")
        self.acceso = Acceso(self.tarjeta, 2, "sds")
        assert self.acceso.validarAcceso() == False

    def testValidarAcceso21(self):
        self.tarjeta = Tarjeta("00222223","Estudiante")
        self.acceso = Acceso(self.tarjeta, "sads", 12)
        assert self.acceso.validarAcceso() == False

    def testValidarAcceso25(self):
        self.tarjeta = Tarjeta("00222223","Empleado")
        self.acceso = Acceso(self.tarjeta, 1, "sdssd")
        assert self.acceso.validarAcceso() == False

    def testValidarAcceso3(self):
        self.tarjeta = Tarjeta("00222223","Estudiante")
        self.acceso = Acceso(self.tarjeta, 1, 34)
        assert self.acceso.validarAcceso() == False

    def testValidarAcceso34(self):
        self.tarjeta = Tarjeta("00222223","Estudiante")
        self.acceso = Acceso(self.tarjeta, 1, 9)
        assert self.acceso.validarAcceso() == True

    def testValidarAcceso35(self):
        self.tarjeta = Tarjeta("00222223","Estudiante")
        self.acceso = Acceso(self.tarjeta, 1, 21)
        assert self.acceso.validarAcceso() == False

    def testValidarAcceso4(self):
        self.tarjeta = Tarjeta("00222223","Estudiante")
        self.acceso = Acceso(self.tarjeta, 7, 10)
        assert self.acceso.validarAcceso() == False

    def testValidarAcceso5(self):
        self.tarjeta = Tarjeta("00222223","Empleado")
        self.acceso = Acceso(self.tarjeta, 1, 11)
        assert self.acceso.validarAcceso() == True

    def testValidarAcceso6(self):
        self.tarjeta = Tarjeta("00222223","Empleado")
        self.acceso = Acceso(self.tarjeta, 1, 9)
        assert self.acceso.validarAcceso() == True

    def testValidarAcceso7(self):
        self.tarjeta = Tarjeta("00222223","Empleado")
        self.acceso = Acceso(self.tarjeta, 10, 9)
        assert self.acceso.validarAcceso() == False
        
    def testValidarHorarioEmpleado1(self):
        self.tarjeta = Tarjeta("12222223","Empleado")
        self.acceso = Acceso(self.tarjeta, 6, 11)
        assert self.acceso.validarAcceso() == True

    def testValidarHorarioEmpleado2(self):
        self.tarjeta = Tarjeta("12222223","Empleado")
        self.acceso = Acceso(self.tarjeta, 6, 9)
        assert self.acceso.validarAcceso() == False
    
if __name__ == "__main__":
    unittest.main()   # run all tests
