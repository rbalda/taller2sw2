import unittest
from acceso import acceso

class SimpleTestCase(unittest.TestCase):
    def testA(self):
        assert acceso("001024a", "11:30:32", 2) == 0
        
    def testB(self):
        assert acceso("00102345", "11:30:32", 2) == 0
    
    def testC(self):
        assert acceso("0010234", "11:30:32", -1) == 0

    def testD(self):
        assert acceso("0010234", "11:30:32", 8) == 0

    def testE(self):
        assert acceso("0010234", "11:30:32", 2) == 1

    def testF(self):
        assert acceso("0010234", "09:30:32", 7) == 0

    def testG(self):
        assert acceso("0010234", "16:30:32", 7) == 0

    def testH(self):
        assert acceso("0010234", "11:30:32", 7) == 1

    def testI(self):
        assert acceso("0110234", "07:30:32", 1) == 0

    def testJ(self):
        assert acceso("0110234", "11:30:32", 1) == 1

    def testK(self):
        assert acceso("0110234", "19:30:32", 1) == 0

    def testL(self):
        assert acceso("0110234", "11:30:32", 7) == 0

        
if __name__ == "__main__":
    unittest.main()
