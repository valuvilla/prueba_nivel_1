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

    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo=tipo

    def __str__(self):
       return Vehiculo.__str__(self) + f", tipo: {self.tipo}"

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga=carga

    def __str__(self):
         return Coche.__str__(self) + f",Carga: {self.carga} kg de carga"
    
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo,)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def __str__(self):
        return Bicicleta.__str__(self) + f", Velocidad: {self.velocidad} km/h, Cilidrada: {self.cilindrada} cc"



bicicleta=Bicicleta("rojo", 2, "urbana")
moto=Motocicleta("negra", 2, "urbana", 180, 600)
coche = Coche("azul", 150, 4, 1200)
print(coche)
print(bicicleta)
print(moto)