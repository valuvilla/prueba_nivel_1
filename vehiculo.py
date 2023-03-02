class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return f"Color: {self.color}, {self.ruedas} ruedas"
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
       return Vehiculo.__str__(self) + f", Velocidad:  {self.velocidad} km/h, cilindrada: {self.cilindrada} cc"

    
    
class Vehiculos():
    lista=[]

    @staticmethod
    def agregar_lista():
        coche=Coche()

