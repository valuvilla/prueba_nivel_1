import config
import csv

class Vehiculo():
    def __init__(self, color, ruedas, num_bastidor):
        self.color = color
        self.ruedas = ruedas
        self.num_bastidor = num_bastidor

    def __str__(self):
        return f"Color: {self.color}, {self.ruedas} ruedas, Número de Bastidor: {self.num_bastidor}"

vehi=Vehiculo("rojo", 4, 123456)
print(vehi)

class Vehiculos():




    

    @staticmethod
    def buscar_vehiculo(num_bastidor):
        # Buscar un vehículo por su número de bastidor
        for vehiculo in Vehiculos.lista:
            if vehiculo.num_bastidor == num_bastidor:
                if vehiculo.ruedas==4:
                    buscar_coche=Coche(vehiculo.color, vehiculo.ruedas, vehiculo.num_bastidor, vehiculo.velocidad, vehiculo.cilindrada)
    
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
    


        
        
    
    


