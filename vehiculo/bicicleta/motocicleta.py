from vehiculo.bicicleta.bicicleta import Bicicleta
import config
import csv

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, num_bastidor, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, num_bastidor, tipo)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def __str__(self):
        return Bicicleta.__str__(self) + f", Velocidad: {self.velocidad} km/h, Cilidrada: {self.cilindrada} cc"