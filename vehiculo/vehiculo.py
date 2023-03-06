import config
import csv






class Vehiculo():
    def __init__(self, color, ruedas, num_bastidor):
        self.color = color
        self.ruedas = ruedas
        self.num_bastidor = num_bastidor

    def __str__(self):
        return f"Color: {self.color}, {self.ruedas} ruedas, Número de Bastidor: {self.num_bastidor}"

import config
import csv

from vehiculo.vehiculo import Vehiculos


class Coche(Vehiculos):
    def __init__(self, color, ruedas,num_bastidor, velocidad, cilindrada):
        super().__init__(color, ruedas, num_bastidor)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
       return super().__str__(self) + f", Velocidad:  {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc"


class Formula1(Coche):
    def __init__(self, color, ruedas, num_bastidor, velocidad, cilindrada, equipo):
        super().__init__(color, ruedas, num_bastidor, velocidad, cilindrada)
        self.equipo=equipo

    def __str__(self):
        return Coche.__str__(self) + f", Equipo: {self.equipo}"
    
class Camioneta(Coche):
    def __init__(self, color, ruedas, num_bastidor, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, num_bastidor, velocidad, cilindrada)
        self.carga=carga

    def __str__(self):
         return Coche.__str__(self) + f",Carga: {self.carga} kg de carga"

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, num_bastidor, tipo):
        super().__init__(color, ruedas, num_bastidor)
        self.tipo=tipo

    def __str__(self):
       return Vehiculo.__str__(self) + f", tipo: {self.tipo}"
    

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, num_bastidor, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, num_bastidor, tipo)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def __str__(self):
        return Bicicleta.__str__(self) + f", Velocidad: {self.velocidad} km/h, Cilidrada: {self.cilindrada} cc"
    

class Vehiculos():
    lista=[]
    with open(config.DATABASE_PATH) as fichero:
        reader=csv.reader(fichero)
        for color, ruedas, num_bastidor, velocidad, cilindrada, carga, equipo, tipo in reader:
            if ruedas==4:
                if carga=="" and equipo=="":
                    lista.append(Coche(color, ruedas, num_bastidor, velocidad, cilindrada))
                elif equipo=="":
                    lista.append(Camioneta(color, ruedas, num_bastidor, velocidad, cilindrada, carga))
                else:
                    lista.append(Formula1(color, ruedas, num_bastidor, velocidad, cilindrada, equipo))
            elif ruedas==2:
                if velocidad=="" and cilindrada=="":
                    lista.append(Bicicleta(color, ruedas, num_bastidor, tipo))
                else:
                    lista.append(Motocicleta(color, ruedas, num_bastidor, tipo, velocidad, cilindrada))

    @staticmethod
    def crear_coche(color, ruedas, num_bastidor, velocidad, cilindrada, carga, equipo):
        if equipo=="" and carga=="":
            coche=Coche(color, ruedas, num_bastidor, velocidad, cilindrada)
            Vehiculos.lista.append(coche)
        elif equipo=="":
            coche=Camioneta(color, ruedas, num_bastidor, velocidad, cilindrada, carga)
            Vehiculos.lista.append(coche)
        else:
            coche=Formula1(color, ruedas, num_bastidor, velocidad, cilindrada, equipo)
            Vehiculos.lista.append(coche)

    staticmethod
    def buscar_coche(num_bastidor):
        for coche in Coches.lista:
            if coche.num_bastidor==num_bastidor:
                print("Coche encontrado")
                if coche.equipo==None and coche.carga==None:
                    return f'Color: {coche.color}, Ruedas: {coche.ruedas}, Numero de bastidor: {coche.num_bastidor}, Velocidad: {coche.velocidad} km/h, Cilindrada: {coche.cilindrada} cc'
                elif coche.carga==None:
                    return f'Color: {coche.color}, Ruedas: {coche.ruedas}, Numero de bastidor: {coche.num_bastidor}, Velocidad: {coche.velocidad} km/h, Cilindrada: {coche.cilindrada} cc, Equipo: {coche.equipo}'
                else:
                
                    return f'Color: {coche.color}, Ruedas: {coche.ruedas}, Numero de bastidor: {coche.num_bastidor}, Velocidad: {coche.velocidad} km/h, Cilindrada: {coche.cilindrada} cc, Carga: {coche.carga} kg de carga'
            

    @staticmethod
    def modificar_coche(color, ruedas, num_bastidor, velocidad, cilindrada, carga, equipo):
        for coche, indice in enumerate(Vehiculos.lista):
            if coche.num_bastidor==num_bastidor:
                Vehiculos.lista[indice].color=color
                Vehiculos.lista[indice].ruedas=ruedas
                Vehiculos.lista[indice].velocidad=velocidad 
                Vehiculos.lista[indice].cilindrada=cilindrada
                Vehiculos.lista[indice].carga=carga
                Vehiculos.lista[indice].equipo=equipo
                print("Coche modificado")
                Vehiculos.guardar_vehiculos()
                return Vehiculos.lista[indice]
            
    @staticmethod
    def modificar_bici(color, ruedas, num_bastidor, tipo):
        for bici, indice in enumerate(Vehiculos.lista):
            if bici.num_bastidor==num_bastidor:
                Vehiculos.lista[indice].color=color
                Vehiculos.lista[indice].ruedas=ruedas
                Vehiculos.lista[indice].tipo=tipo
                print("Bici modificada")
                Vehiculos.guardar_vehiculos()
                return Vehiculos.lista[indice]
            
    


    @staticmethod
    def crear_bici(color, ruedas, num_bastidor, velocidad, cilindrada, tipo):
        if velocidad=="" and cilindrada=="":
            bici=Bicicleta(color, ruedas, num_bastidor, tipo)
            Vehiculos.lista.append(bici)
        else:
            bici=Motocicleta(color, ruedas, num_bastidor, tipo, velocidad, cilindrada)
            Vehiculos.lista.append(bici)

    @staticmethod
    def buscar_bici(num_bastidor):
        for bici in Bicis.lista:
            if bici.num_bastidor==num_bastidor:
                print("Bici encontrada")
                if bici.tipo==None:
                    return f'Color: {bici.color}, Ruedas: {bici.ruedas}, Numero de bastidor: {bici.num_bastidor}'
                elif bici.velocidad==None:
                    return f'Color: {bici.color}, Ruedas: {bici.ruedas}, Numero de bastidor: {bici.num_bastidor}, Tipo: {bici.tipo}'
                else:
                    return f'Color: {bici.color}, Ruedas: {bici.ruedas}, Numero de bastidor: {bici.num_bastidor}, Velocidad: {bici.velocidad} km/h, Cilindrada: {bici.cilindrada} cc, Tipo: {bici.tipo}'




    @staticmethod
    def buscar_vehiculo(num_bastidor):
        for vehiculo in Vehiculos.lista:
            if vehiculo.num_bastidor==num_bastidor:
                print("Vehículo encontrado")
                if vehiculo.ruedas==4:
                    Vehiculos.buscar_coche(num_bastidor)
                elif vehiculo.ruedas==2:
                    Vehiculos.buscar_bici(num_bastidor)

    @staticmethod
    def listar_vehiculos():
        for vehiculo in Vehiculos.lista:
            print(vehiculo)



    @staticmethod
    def eliminar_vehiculo(num_bastidor):
        for vehiculo in Vehiculos.lista:
            if vehiculo.num_bastidor==num_bastidor:
                Vehiculos.lista.remove(vehiculo)
                print("Vehículo eliminado")
    
    @staticmethod
    def modificar_vehiculo(num_bastidor):
        for vehiculo in Vehiculos.lista:
            if vehiculo.num_bastidor==num_bastidor:
                print("Vehículo encontrado")
                if vehiculo.ruedas==4:
                    Vehiculos.modificar_coche(num_bastidor)
                elif vehiculo.ruedas==2:
                    Vehiculos.modificar_bici(num_bastidor)

    @staticmethod
    def guardar_vehiculos():
        with open(config.DATABASE_PATH, "w") as fichero:
            writer=csv.writer(fichero)
            for vehiculo in Vehiculos.lista:
                writer.writerow(vehiculo)

    

            