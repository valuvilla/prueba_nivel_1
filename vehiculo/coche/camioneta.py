from vehiculo.coche.coche import Coche
import config
import csv

class Camioneta(Coche):
    def __init__(self, color, ruedas, num_bastidor, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, num_bastidor, velocidad, cilindrada)
        self.carga=carga

    def __str__(self):
         return Coche.__str__(self) + f",Carga: {self.carga} kg de carga"