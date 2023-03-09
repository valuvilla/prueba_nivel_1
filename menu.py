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
            nu = None
            while True:
                num_bastidor = helpers.leer_texto(3, 3, "num_bastidor (2 int y 1 char)").upper()
                if re.match('[0-9]{2}[A-Z]$', num_bastidor):
                    break
            vehiculo = db.Vehiculos.buscar(num_bastidor)
            print(vehiculo) if vehiculo else print(Fore.RED+f"Cliente de num_bastidor: {num_bastidor} no encontrado.")

        elif opcion == "3":
            print(Back.LIGHTGREEN_EX+"Añadiendo un cliente...\n")

            num_bastidor = None
            while True:
                num_bastidori = helpers.leer_texto(3, 3, "num_bastidorI (2 int y 1 char)").upper()
                if helpers.num_bastidor_válido(num_bastidori, db.Clientes.lista):
                    break

            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 chars)").capitalize()
            db.Clientes.agregar_cliente(num_bastidori, nombre, apellido)
            print((Back.GREEN+"\nCliente añadido correctamente"), (Fore.GREEN+'\nDatos del cliente:'))
            print(f"num_bastidorI: {num_bastidori} \nNombre: {nombre} \nApellido: {apellido}")
