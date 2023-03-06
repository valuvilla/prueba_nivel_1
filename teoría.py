
import config
import csv

class Vehiculo():
    def __init__(self, color, ruedas, num_bastidor):
        self.color = color
        self.ruedas = ruedas
        self.num_bastidor = num_bastidor
    def __str__(self):
        return f"Color: {self.color}, {self.ruedas} ruedas, Número de Bastidor: {self.num_bastidor}"

class Coche(Vehiculo):
    def __init__(self, color, ruedas,num_bastidor, velocidad, cilindrada):
        super().__init__(color, ruedas, num_bastidor)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
       return super().__str__(self) + f", Velocidad:  {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc"

    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, num_bastidor, tipo):
        super().__init__(color, ruedas, num_bastidor)
        self.tipo=tipo

    def __str__(self):
       return Vehiculo.__str__(self) + f", tipo: {self.tipo}"

class Camioneta(Coche):
    def __init__(self, color, ruedas, num_bastidor, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, num_bastidor, velocidad, cilindrada)
        self.carga=carga

    def __str__(self):
         return Coche.__str__(self) + f",Carga: {self.carga} kg de carga"
    
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, num_bastidor, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, num_bastidor, tipo)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def __str__(self):
        return Bicicleta.__str__(self) + f", Velocidad: {self.velocidad} km/h, Cilidrada: {self.cilindrada} cc"

class Formula1(Coche):
    def __init__(self, color, ruedas, num_bastidor, velocidad, cilindrada, equipo):
        super().__init__(color, ruedas, num_bastidor, velocidad, cilindrada)
        self.equipo=equipo

    def __str__(self):
        return Coche.__str__(self) + f", Equipo: {self.equipo}"
    

# busqueda de bastidores
# busqueda por tipos
# busqueda por ruedas
# busqueda por cilindrada
# busqueda por velocidad


class Vehiculos():

    lista=[]
    with open(config.DATABASE_PATH, "r") as file:
        reader=csv.reader(file)
        for num_bastidores,


    

    @staticmethod
    def buscar_vehiculo(num_bastidor):
        # Buscar un vehículo por su número de bastidor
        for vehiculo in Vehiculos.lista:
            if vehiculo.num_bastidor == num_bastidor:
                if vehiculo.ruedas==4:
                    if vehiculo.carga==None:
                        return Coche(vehiculo.color, vehiculo.ruedas, vehiculo.num_bastidor, vehiculo.velocidad, vehiculo.cilindrada)
                    else:
                        return Camioneta(vehiculo.color, vehiculo.ruedas, vehiculo.num_bastidor, vehiculo.velocidad, vehiculo.cilindrada, vehiculo.carga)
                elif vehiculo.ruedas==2:
                    if vehiculo.tipo=="urbana":
                        return Bicicleta(vehiculo.color, vehiculo.ruedas, vehiculo.num_bastidor, vehiculo.tipo)
                    elif vehiculo.tipo=="deportiva":
                        return Motocicleta(vehiculo.color, vehiculo.ruedas, vehiculo.num_bastidor, vehiculo.tipo, vehiculo.velocidad, vehiculo.cilindrada)
    
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
    


        
        
    
    


