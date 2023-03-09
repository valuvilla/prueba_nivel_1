import re
import helpers
from colorama import Fore, Back, Style, init
from termcolor import colored
import database as db
init(autoreset=True)

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        lineas=(Fore.BLUE +"="*50)
        print(lineas)
        print(colored((("Bienvenido al menú de vehículos").upper()).center(50), "white", "on_blue"))
        print(lineas)
        print(colored(Fore.BLUE+"[1]"),"Listar vehículos")
        print(colored(Fore.BLUE+"[2]"),"Buscar vehículo")
        print(colored(Fore.BLUE+"[3]"),"Agregar vehículo")
        print(colored(Fore.BLUE+"[4]"),"Eliminar vehículo")
        print(colored(Fore.BLUE+"[5]"),"Catalogar vehículo")
        print(colored(Fore.RED+"[6]"),("SALIR"))
        print(lineas)

        opcion = input(colored(Fore.BLUE+"Elige una opción: ", "blue"))
        helpers.limpiar_pantalla()

        if opcion == "1":
            print(Back.CYAN+Fore.WHITE+"Listar vehículos")
            # Listar vehiculos
            for vehiculo in db.Vehiculos.lista:
                print(f'{type(vehiculo).__name__} {vehiculo}')
            
        elif opcion == "2":
            print(Back.CYAN+Fore.WHITE+"Buscar vehículo")
            num_bastidor = None
            while True:
                num_bastidor = helpers.leer_texto(3, 3, "num_bastidor (2 int y 1 char)").upper()
                if helpers.num_bastidor_valido(num_bastidor, db.Vehiculos.lista):
                    break
            vehiculo = db.Vehiculos.buscar(num_bastidor)
            print(vehiculo) if vehiculo else print(Fore.RED+f"Cliente de num_bastidor: {num_bastidor} no encontrado.")

        elif opcion == "3":
            print(Back.LIGHTGREEN_EX+"Añadiendo un cliente...\n")

            helpers.limpiar_pantalla()

            lineas=(Fore.BLUE +"="*50)
            print(lineas)
            print(colored((("Bienvenido al menú de crear vehículos").upper()).center(50), "white", "on_blue"))
            print(lineas)
            print(colored(Fore.BLUE+"[1]"),"Coche")
            print(colored(Fore.BLUE+"[2]"),"Bicicleta")
            print(colored(Fore.BLUE+"[3]"),"Formula 1")
            print(colored(Fore.BLUE+"[4]"),"Camioneta")
            print(colored(Fore.BLUE+"[5]"),"Moto")
            print(colored(Fore.BLUE+"[6]"),"Quad")
            print(colored(Fore.RED+"[7]"),("SALIR"))
            print(lineas)

            opcion = input(colored(Fore.BLUE+"Elige una opción: ", "blue"))
            helpers.limpiar_pantalla()

            num_bastidor = None
            while True:
                num_bastidor = helpers.leer_texto(3, 3, "num_bastidor (2 int y 1 char)").upper()
                if helpers.num_bastidor_valido(num_bastidor, db.Vehiculos.lista):
                    break
            
            color= helpers.leer_texto(2, 30, "Color (de 2 a 30 chars)").capitalize()
            ruedas = helpers.validar_ruedas("Ruedas (de 2 o 4): ")

            if opcion == "1":
                velocidad= helpers.leer_numero(0, 250, "Velocidad (de 0 a 250): ")
                cilindrada= helpers.leer_numero(0, 10000, "Cilindrada (de 0 a 10000): ")
                db.Vehiculos.crear("Coche", num_bastidor, color, ruedas, velocidad, cilindrada)
                print(Back.GREEN+"Coche creado correctamente")


            
        
        elif opcion == '6':
            print(Back.MAGENTA+"SALIENDO\n")
            break

        input("\nPresiona ENTER para continuar...")

iniciar()