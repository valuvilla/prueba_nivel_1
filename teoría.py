import config
import csv

class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return f"Color: {self.color}, {self.ruedas} ruedas"

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada,tipo_vehiculo):
        super().__init__(color, ruedas)
        self.tipo_vehiculo="Coche"
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
       return Vehiculo.__str__(self) + f", Velocidad:  {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc, Tipo de vehiculo: {self.tipo_vehiculo}"

    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo, tipo_vehiculo):
        super().__init__(color, ruedas)
        self.tipo_vehiculo="Bicicleta"
        self.tipo=tipo

    def __str__(self):
       return Vehiculo.__str__(self) + f", tipo: {self.tipo}, Tipo de vehiculo: {self.tipo_vehiculo}"

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga, tipo_vehiculo):
        super().__init__(color, ruedas, velocidad, cilindrada, tipo_vehiculo)
        self.carga=carga

    def __str__(self):
         return Coche.__str__(self) + f",Carga: {self.carga} kg de carga"
    
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada, tipo_vehiculo):
        super().__init__(color, ruedas, tipo, tipo_vehiculo)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def __str__(self):
        return Bicicleta.__str__(self) + f", Velocidad: {self.velocidad} km/h, Cilidrada: {self.cilindrada} cc"

#  Crea al menos un objetios de cada clase y añadelos a una lista


class Vehiculos():

    lista=[]
    with open(config.DATABASE_PATH, "r") as file:
        reader=csv.reader(file, delimiter=";")
        for color, ruedas, velocidad, cilindrada, tipo, carga, tipo_vehiculo in reader:
            if tipo_vehiculo=="Coche":
                if carga==None:
                    vehiculo=Coche(color, ruedas, velocidad, cilindrada,tipo_vehiculo)
                vehiculo=Camioneta(color, ruedas, velocidad, cilindrada,carga)
            elif tipo_vehiculo=="Bicicleta":
                if velocidad==None:
                    vehiculo=Bicicleta(color, ruedas, tipo, tipo_vehiculo)
                vehiculo=Motocicleta(color, ruedas, tipo, velocidad, cilindrada)
            lista.append(vehiculo)

    

    @staticmethod
    def agregar_lista(color, ruedas, velocidad, cilindrada,tipo,carga,tipo_vehiculo):
        # Definir el tipo de vehiculo
        if tipo_vehiculo=="Coche":
            if carga==None:
                vehiculo=Coche(color, ruedas, velocidad, cilindrada,tipo_vehiculo)
            vehiculo=Camioneta(color, ruedas, velocidad, cilindrada,carga)
        elif tipo_vehiculo=="Bicicleta":
            if velocidad==None:
                vehiculo=Bicicleta(color, ruedas, tipo, tipo_vehiculo)
            vehiculo=Motocicleta(color, ruedas, tipo, velocidad, cilindrada)
        Vehiculos.lista.append(vehiculo)
        return vehiculo
    


    


