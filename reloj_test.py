import unittest
from reloj import Reloj

class TestAlarma(unittest.TestCase):

    def test_suena_en_hora(self):
            reloj = Reloj()
            reloj.definir_alarma('08:00')
            reloj.prender()
            sonar = reloj.sonar('08:00')
            self.assertTrue(sonar)

if __name__ == '__main__':
    unittest.main()