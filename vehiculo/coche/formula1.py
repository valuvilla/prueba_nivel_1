import config
import csv



class Formula1(Coche):
    def __init__(self, color, ruedas, num_bastidor, velocidad, cilindrada, equipo):
        super().__init__(color, ruedas, num_bastidor, velocidad, cilindrada)
        self.equipo=equipo

    def __str__(self):
        return Coche.__str__(self) + f", Equipo: {self.equipo}"