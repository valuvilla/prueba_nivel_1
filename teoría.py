class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color=color
        self.ruedas=ruedas
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def __str__(self):
       return "color {}, {} km/h, {} ruedas, {} cc".format(
self.color, self.velocidad, self.ruedas, self.cilindrada )
    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        self.color=color
        self.ruedas=ruedas
        self.tipo=tipo

    def __str__(self):
       return "color {}, {} ruedas, {} ".format(
self.color, self.ruedas, self.tipo
       )

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        self.color=color
        self.ruedas=ruedas
        self.velocidad=velocidad
        self.cilindrada=cilindrada
        self.carga=carga

    def __str__(self):
         return "color {}, {} km/h, {} ruedas, {} cc, {} kg".format(
self.color, self.velocidad, self.ruedas, self.cilindrada, self.carga )
    
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        self.color=color
        self.ruedas=ruedas
        self.tipo=tipo
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def __str__(self):
         return "color {}, {} km/h, {} ruedas, {} cc".format(
self.color, self.velocidad, self.ruedas, self.cilindrada )
    

coche = Coche("azul", 150, 4, 1200)
print(coche)