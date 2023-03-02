import csv
import copy
import config
import helpers
import unittest
import teoría as vl

class testVehiculo(unittest.TestCare):

    def setUp(self):
        vl.Vehiculos.lista = [
            vl.Coche("rojo", 4, 120, 1200, "Coche"),
            vl.Bicicleta("azul", 2, "urbana", "Bicicleta"),
            vl.Camioneta("verde", 4, 100, 1000, 1000, "Coche"),
            vl.Motocicleta("verde", 2, "urbana", 100, 1000, "Bicicleta")
        ]

    def test_agregar_lista(self):
    
        vl.Vehiculos.agregar_lista("rojo", 4, 120, 1200, "Coche", None, "Coche")