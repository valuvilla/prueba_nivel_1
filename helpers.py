import re
import os
import sys
import platform

from colorama import Back

def limpiar_pantalla() -> None:
    os.system('cls') if platform.system() == "Windows" else os.system('clear')


def leer_numero(min=0, max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        try:
            numero = input("> ")
            if int(numero) >= min and int(numero) <= max:
                return numero
        except ValueError:
            pass


def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("Ingrese un texto: ")
        if len(texto) < longitud_min or len(texto) > longitud_max:
            print(f"Error, debe ingresar un texto entre {longitud_min} y {longitud_max} caracteres")
        else:
            return texto
        

def num_bastidor_valido(num_bastidor, lista):
    #comprobar que el dni tiene el formato correcto
    if not re.match('[0-9]{2}[A-Z]$', num_bastidor):
        print(Back.RED+f"El formato de numero de bastidor {num_bastidor} no es correcto")
        return False
    #comprobar que el dni no está en la lista
    for vehiculo in lista:
        if vehiculo.num_bastidor_ == num_bastidor:
            print(Back.RED+f"El Número de Bastidor: {num_bastidor} ya existe")
            return False
    return True

def validar_ruedas(mensaje: str) -> int:
    while True:
        try:
            numero = int(input(mensaje))
            # numero distinto de 2 y 4
            if numero != 2 and numero != 4:
                print("Error, debe ingresar 2 o 4 ruedas")
            else:
                return numero
        except ValueError:
            print("Error, debe ingresar un número entero")

