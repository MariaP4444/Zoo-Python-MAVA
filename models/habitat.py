import streamlit as st


class Habitat:
    def __init__(self, nombre = "", tempMax = 0, tempMin = 0 , dieta = None, cantMaxAnimales = 0):
        self.nombre = nombre
        self.tempMax = tempMax
        self.tempMin = tempMin
        self.animales = {}
        self.dieta = dieta
        self.cantMaxAnimales = cantMaxAnimales


    """ LISTAR ANIMALES
     Opcion: Vincular animal
     Dado un objeto animal, lo agrega al diccionario de animales del habitat, la clave es el ID y el valor el objeto animal
    """
    def agregarAnimal(self, animalNuevo):
        self.animales[animalNuevo.id] = animalNuevo


class HabitatAcuatico(Habitat):
    def __init__(self,  nombre, tempMax, tempMin, dieta, cantMaxAnimales, salinidad, profundidad):
        super().__init__( nombre, tempMax, tempMin,dieta, cantMaxAnimales)
        self.salinidad = salinidad
        self.profundidad = profundidad




class HabitatPolar(Habitat):
    def __init__(self, nombre, tempMax, tempMin,dieta, cantMaxAnimales, cantidadHielo, tamanioCueva):
        super().__init__( nombre, tempMax, tempMin,dieta, cantMaxAnimales)
        self.cantidadHielo = cantidadHielo
        self.tamanioCueva = tamanioCueva




class HabitatDesertico(Habitat):
    def __init__(self,  nombre, tempMax, tempMin,dieta, cantMaxAnimales, humedad, cantidadOasis):
        super().__init__( nombre, tempMax, tempMin,dieta, cantMaxAnimales)
        self.humedad = humedad
        self.cantidadOasis = cantidadOasis
    



class HabitatSelvatico(Habitat):
    def __init__(self,  nombre, tempMax, tempMin,dieta, cantMaxAnimales, cantidadArboles, cantidadRios):
        super().__init__( nombre, tempMax, tempMin,dieta, cantMaxAnimales)
        self.cantidadArboles = cantidadArboles
        self.cantidadRios = cantidadRios

