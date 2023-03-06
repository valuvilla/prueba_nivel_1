import re
import helpers
from colorama import Fore, Back, Style
from termcolor import colored
import database as db

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
            # Listar vehiculos
            db.Vehiculos.listar_vehiculos()
            
            
        elif opcion == "2":
            print(Back.CYAN+Fore.WHITE+"Buscar vehículo")
            num_bastidor=None
            while True:
                num_bastidor=helpers.Numero_Bastidor_Válido(input("Introduce el número de bastidor: "), db.Vehiculos.lista)
                if re.match('[0-9]{2}[A-Z]$', num_bastidor):
                    break
                vehiculo=db.Vehiculos.buscar_vehiculo(num_bastidor)
                print(vehiculo) if vehiculo else print("No se ha encontrado el vehículo")


            
        elif opcion == "3":
            print(Back.CYAN+Fore.WHITE+"Agregar vehículo")
            # Agregar vehiculo
            tipo_vehuclo=None
            while True:
                tipo_vehuclo=input("Introduce el tipo de vehículo:  C/B ").lower()
                if tipo_vehuclo=="c" or tipo_vehuclo=="m":
                    break
            if tipo_vehuclo=="c":
                num_bastidor=helpers.Numero_Bastidor_Válido(input("Introduce el número de bastidor: "), db.Vehiculos.lista)
                color=input("Introduce el color: ")
                
                
                db.Vehiculos.agregar_vehiculo(db.Coche(num_bastidor, marca, modelo, color, precio, num_puertas))

            
        elif opcion == "4":
            print(Back.CYAN+Fore.WHITE+"Eliminar vehículo")
            num_bastidor=helpers.Numero_Bastidor_Válido(input("Introduce el número de bastidor: "), Vehiculos.lista)
            print(f'Vehículo con número de bastidor {num_bastidor} eliminado') if Vehiculos.eliminar_vehiculo(num_bastidor) else print("No se ha encontrado el vehículo")

        

            

        elif opcion == "5":
            print(colored(Fore.RED+"Saliendo..."))
            break

        input("\nPresiona ENTER para continuar...")
        
iniciar()