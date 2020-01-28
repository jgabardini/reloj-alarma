
from datetime import datetime

class Reloj:
    def __init__(self):
        self.prendida = False
        self.alarma = None

    def definir_alarma(self, hora):
        self.alarma = datetime.strptime(hora, '%H:%M')

    def prender(self):
        self.prendida = True

    def apagar(self):
        self.prendida = False

    def sonar(self, hora):
        ahora = datetime.strptime(hora, '%H:%M')
        return self.prendida and self.alarma.hour == ahora.hour and self.alarma.min == ahora.min
