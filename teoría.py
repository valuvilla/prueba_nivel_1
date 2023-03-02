import config
import csv

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
       return Vehiculo.__str__(self) + f", Velocidad:  {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc"

    
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
        super().__init__(color, ruedas, tipo)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def __str__(self):
        return Bicicleta.__str__(self) + f", Velocidad: {self.velocidad} km/h, Cilidrada: {self.cilindrada} cc"

#  Crea al menos un objetios de cada clase y añadelos a una lista


class Vehiculos():

    lista_coche=[]
    lista_bicicleta=[]
    with open(config.DATABASE_PATH, "r") as file:


    

    @staticmethod
    def buscar_vehiculo(ruedas):
        for vehiculo in Vehiculos.lista_coche:
            if vehiculo.ruedas == ruedas:
                return vehiculo
        for vehiculo in Vehiculos.lista_bicicleta:
            if vehiculo.ruedas == ruedas:
                return vehiculo
        return None
    
    @staticmethod
    def agregar_lista(color, ruedas, velocidad, cilindrada, tipo, carga):
        if ruedas == 4:
            if carga == None:
                coche=Coche(color, ruedas, velocidad, cilindrada)
                Vehiculos.lista_coche.append(coche)
                return coche
            else:
                camioneta=Camioneta(color, ruedas, velocidad, cilindrada, carga)
                Vehiculos.lista_coche.append(camioneta)
                return camioneta
        elif ruedas == 2:
            if tipo == "urbana":
                bicicleta=Bicicleta(color, ruedas, tipo)
                Vehiculos.lista_bicicleta.append(bicicleta)
                return bicicleta
            elif tipo == "deportiva":
                motocicleta=Motocicleta(color, ruedas, tipo, velocidad, cilindrada)
                Vehiculos.lista_bicicleta.append(motocicleta)
                return motocicleta
        else:
            return "No se puede agregar el vehiculo"
        
    @staticmethod
    def catalogar():
        ruedas=0
        for vehiculo in Vehiculos.lista_coche:
            ruedas+=vehiculo.ruedas
        for vehiculo in Vehiculos.lista_bicicleta:
            ruedas+=vehiculo.ruedas
        return f'Hay {len(Vehiculos.lista_coche)+len(Vehiculos.lista_bicicleta)} vehiculos y {ruedas} ruedas en total'
    
    
    '
        
        
    
    


