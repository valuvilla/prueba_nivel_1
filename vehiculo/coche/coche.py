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

class Coches:
    lista=[]
    with open(config.DATABASE_PATH) as fichero:
        reader=csv.reader(fichero)
        for  color, ruedas, num_bastidor, velocidad, cilindrada, carga, equipo in reader:
            lista.append(Coche(color, ruedas, num_bastidor, velocidad, cilindrada, carga, equipo))

    

    @staticmethod
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
    def mostrar_coches():
        for coche in Coches.lista:
            if coche.equipo==None and coche.carga==None:
                print(f'Color: {coche.color}, Ruedas: {coche.ruedas}, Numero de bastidor: {coche.num_bastidor}, Velocidad: {coche.velocidad} km/h, Cilindrada: {coche.cilindrada} cc')
            elif coche.carga==None:
                print(f'Color: {coche.color}, Ruedas: {coche.ruedas}, Numero de bastidor: {coche.num_bastidor}, Velocidad: {coche.velocidad} km/h, Cilindrada: {coche.cilindrada} cc, Equipo: {coche.equipo}')
            else:
                print(f'Color: {coche.color}, Ruedas: {coche.ruedas}, Numero de bastidor: {coche.num_bastidor}, Velocidad: {coche.velocidad} km/h, Cilindrada: {coche.cilindrada} cc, Carga: {coche.carga} kg de carga')

    @staticmethod
    def crear_coche():
        color=input("Color: ")
        ruedas=input("Ruedas: ")
        num_bastidor=input("Numero de bastidor: ")
        velocidad=input("Velocidad: ")
        cilindrada=input("Cilindrada: ")
        equipo=input("Equipo: ")
        carga=input("Carga: ")
        if equipo=="" and carga=="":
            coche=Coche(color, ruedas, num_bastidor, velocidad, cilindrada)
            Coches.lista.append(coche)
        elif equipo=="":
            coche=Camioneta(color, ruedas, num_bastidor, velocidad, cilindrada, carga)
            Coches.lista.append(coche)
        else:
            coche=Formula1(color, ruedas, num_bastidor, velocidad, cilindrada, equipo)
            Coches.lista.append(coche)

    @staticmethod
    def eliminar_coche():
        num_bastidor=input("Numero de bastidor: ")
        for coche in Coches.lista:
            if coche.num_bastidor==num_bastidor:
                Coches.lista.remove(coche)
                print("Coche eliminado")

    @staticmethod
    def guardar_coches():
        with open(config.DATABASE_PATH, "w") as fichero:
            writer=csv.writer(fichero)
            for coche in Coches.lista:
                if coche.equipo==None and coche.carga==None:
                    writer.writerow([coche.color, coche.ruedas, coche.num_bastidor, coche.velocidad, coche.cilindrada])
                elif coche.carga==None:
                    writer.writerow([coche.color, coche.ruedas, coche.num_bastidor, coche.velocidad, coche.cilindrada, coche.equipo])
                else:
                    writer.writerow([coche.color, coche.ruedas, coche.num_bastidor, coche.velocidad, coche.cilindrada, coche.carga])