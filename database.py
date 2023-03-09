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
    
class Quad(Coche):
    def __init__(self, color, ruedas, num_bastidor, velocidad, cilindrada, tipo, modelo, carga):
        super().__init__(color, ruedas, num_bastidor, velocidad, cilindrada)
        self.tipo=tipo
        self.modelo=modelo
        self.carga=carga

    def __str__(self):
        return Coche.__str__(self) + f", Tipo: {self.tipo}, Modelo: {self.modelo}, Carga: {self.carga} kg de carga"
    
class Vehiculos():
    lista=[]
    with open(config.DATABASE_PATH) as fichero:
        reader=csv.reader(fichero)
        for tipo_v in reader:
            if tipo_v=="Coche":
                coche=Coche(*tipo_v[1:])
                lista.append(coche)
            elif tipo_v=="Formula1":
                coche=Formula1(*tipo_v[1:])
                lista.append(coche)
            elif tipo_v=="Camioneta":
                coche=Camioneta(*tipo_v[1:])
                lista.append(coche)
            elif tipo_v=="Bicicleta":
                coche=Bicicleta(*tipo_v[1:])
                lista.append(coche)
            elif tipo_v=="Motocicleta":
                coche=Motocicleta(*tipo_v[1:])
                lista.append(coche)
            elif tipo_v=="Quad":
                coche=Quad(*tipo_v[1:])
                lista.append(coche)

    @staticmethod
    def buscar(id):
        for vehiculo in Vehiculos.lista:
            if vehiculo.id == id:
                return vehiculo

    @staticmethod
    def crear(opcion, *args):
        if opcion == "1":
            vehiculo = Coche(*args)
        elif opcion == "2":
            vehiculo = Bicicleta(*args)
        elif opcion == "3":
            vehiculo = Formula1(*args)
        elif opcion == "4":
            vehiculo = Camioneta(*args)
        elif opcion == "5":
            vehiculo = Motocicleta(*args)
        elif opcion == "6":
            vehiculo = Quad(*args)
        Vehiculos.lista.append(vehiculo)
        Vehiculos.guardar()
        return vehiculo

    @staticmethod
    def borrar(id):
        for indice, vehiculo in enumerate(Vehiculos.lista):
            if vehiculo.id == id:
                vehiculo = Vehiculos.lista.pop(indice)
                Vehiculos.guardar()
                return vehiculo

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for vehiculo in Vehiculos.lista:
                if type(vehiculo)._name_ == "Coche":
                    writer.writerow((type(vehiculo)._name_, vehiculo.id, vehiculo.color, vehiculo.ruedas, vehiculo.velocidad, vehiculo.cilindrada))
                elif type(vehiculo)._name_ == "Bicicleta":
                    writer.writerow((type(vehiculo)._name_, vehiculo.id, vehiculo.color, vehiculo.ruedas, vehiculo.tipo))
                elif type(vehiculo)._name_ == "Formula1":
                    writer.writerow((type(vehiculo)._name_, vehiculo.id, vehiculo.color, vehiculo.ruedas, vehiculo.velocidad, vehiculo.cilindrada, vehiculo.equipo))
                elif type(vehiculo)._name_ == "Camioneta":
                    writer.writerow((type(vehiculo)._name_, vehiculo.id, vehiculo.color, vehiculo.ruedas, vehiculo.velocidad, vehiculo.cilindrada, vehiculo.carga))
                elif type(vehiculo)._name_ == "Motocicleta":
                    writer.writerow((type(vehiculo)._name_, vehiculo.id, vehiculo.color, vehiculo.ruedas, vehiculo.tipo, vehiculo.velocidad, vehiculo.cilindrada))
                elif type(vehiculo)._name_ == "Quad":
                    writer.writerow((type(vehiculo)._name_, vehiculo.id, vehiculo.color, vehiculo.ruedas, vehiculo.velocidad, vehiculo.cilindrada, vehiculo.tipo, vehiculo.modelo, vehiculo.carga))