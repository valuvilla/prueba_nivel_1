import helpers
from colorama import Fore, Back, Style
from termcolor import colored
import vehiculo.vehiculo as Vehiculos


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
            print("Coches:")
            Vehiculos.mostrar_coches()
            print("Bicicletas:")
            Vehiculos.mostrar_bicis()
            
            
        elif opcion == "2":
            print(Back.CYAN+Fore.WHITE+"Buscar vehículo")
            num_bastidor=helpers.Numero_Bastidor_Válido(input("Introduce el número de bastidor: "), Vehiculos.lista)

            for vehiculo in Vehiculos.lista:
                if vehiculo.num_bastidor==num_bastidor:
                    print("Vehículo encontrado")
                    Vehiculos.buscar_vehiculo(num_bastidor)
            
        elif opcion == "3":
            print(Back.CYAN+Fore.WHITE+"Agregar vehículo")
            tipo_vehiculo=helpers.limpiar_pantalla(input("Introduce el tipo de vehículo (C)Coche o (B)Bicicleta: "))            
            if tipo_vehiculo=="C":
                Vehiculos.crear_coche()
            elif tipo_vehiculo=="B":
                Vehiculos.crear_bici()
            
        elif opcion == "4":
            print(Back.CYAN+Fore.WHITE+"Eliminar vehículo")
            num_bastidor=helpers.Numero_Bastidor_Válido(input("Introduce el número de bastidor: "), Vehiculos.lista)
            print(f'Vehículo con número de bastidor {num_bastidor} eliminado') if Vehiculos.eliminar_vehiculo(num_bastidor) else print("No se ha encontrado el vehículo")

        

            

        elif opcion == "5":
            print(colored(Fore.RED+"Saliendo..."))
            break

        input("\nPresiona ENTER para continuar...")
        
iniciar()