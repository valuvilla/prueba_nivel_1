import helpers
from colorama import Fore, Back, Style
from termcolor import colored


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
        print(colored(Fore.RED+"[5]"),("SALIR"))
        print(lineas)

        opcion = input(colored(Fore.BLUE+"Elige una opción: ", "blue"))
        helpers.limpiar_pantalla()

        if opcion == "1":
            print(Back.CYAN+Fore.WHITE+"Listar vehículos")
            
        elif opcion == "2":
            print(Back.CYAN+Fore.WHITE+"Buscar vehículo")
            
        elif opcion == "3":
            print(Back.CYAN+Fore.WHITE+"Agregar vehículo")
            
        elif opcion == "4":
            print(Back.CYAN+Fore.WHITE+"Eliminar vehículo")
            

        elif opcion == "5":
            print(colored(Fore.RED+"Saliendo..."))
            break

iniciar()