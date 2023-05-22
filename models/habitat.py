import streamlit as st


class Habitat:
    def __init__(self, nombre = "", tempMax = 0, tempMin = 0 , dieta = None, cantMaxAnimales = 0):
        self.nombre = nombre
        self.tempMax = tempMax
        self.tempMin = tempMin
        self.animales = {}
        self.dieta = dieta
        self.cantMaxAnimales = cantMaxAnimales


    def devolverPunteroAn(self, id):
        return self.animales[id]

    def listarAnimales(self):
        animalesH = []
        for ID, animal in self.animales.items():
            texto = "++ Id:" + str(ID) + " ++ " + "Nombre: " + self.animales[ID].nombre +" ++ " + "dieta: " + self.animales[ID].alimentacion.tipoDieta
            animalesH.append(texto)

        if animalesH:
            return animalesH

    def agregarAnimal(self, animalNuevo):
        self.animales[animalNuevo.id] = animalNuevo


class HabitatAcuatico(Habitat):
    def __init__(self,  nombre, tempMax, tempMin, dieta, cantMaxAnimales, salinidad, profundidad):
        super().__init__( nombre, tempMax, tempMin,dieta, cantMaxAnimales)
        self.salinidad = salinidad
        self.profundidad = profundidad

    def listarAnimales(self):
        super().listarAnimales()


class HabitatPolar(Habitat):
    def __init__(self, nombre, tempMax, tempMin,dieta, cantMaxAnimales, cantidadHielo, tamanioCueva):
        super().__init__( nombre, tempMax, tempMin,dieta, cantMaxAnimales)
        self.cantidadHielo = cantidadHielo
        self.tamanioCueva = tamanioCueva

    def listarAnimales(self):
        super().listarAnimales()


class HabitatDesertico(Habitat):
    def __init__(self,  nombre, tempMax, tempMin,dieta, cantMaxAnimales, humedad, cantidadOasis):
        super().__init__( nombre, tempMax, tempMin,dieta, cantMaxAnimales)
        self.humedad = humedad
        self.cantidadOasis = cantidadOasis
    
    def listarAnimales(self):
        super().listarAnimales()


class HabitatSelvatico(Habitat):
    def __init__(self,  nombre, tempMax, tempMin,dieta, cantMaxAnimales, cantidadArboles, cantidadRios):
        super().__init__( nombre, tempMax, tempMin,dieta, cantMaxAnimales)
        self.cantidadArboles = cantidadArboles
        self.cantidadRios = cantidadRios

    def listarAnimales(self):
        super().listarAnimales()