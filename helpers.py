import re
import os
import sys
import platform

def limpiar_pantalla() -> None:
    os.system('cls') if platform.system() == "Windows" else os.system('clear')
