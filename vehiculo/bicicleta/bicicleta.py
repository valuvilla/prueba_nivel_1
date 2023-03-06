import config
import csv

from vehiculo.vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, num_bastidor, tipo):
        super().__init__(color, ruedas, num_bastidor)
        self.tipo=tipo

    def __str__(self):
       return Vehiculo.__str__(self) + f", tipo: {self.tipo}"
