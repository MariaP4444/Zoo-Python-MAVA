
class Habitat:
    def __init__(self, nombre, tempMax, tempMin,dieta, cantMaxAnimales):
        self.nombre = nombre
        self.tempMax = tempMax
        self.tempMin = tempMin
        self.animales = {}
        self.dieta = dieta
        self.cantMaxAnimales = cantMaxAnimales


    def devolverPunteroAn(self, id):
        return self.animales[id]

    def listarAnimales(self):
        print("Los animales de este hábitat son:")
        for ID, animal in self.animales.items():
            print("- Nombre:", animal.getNombre())
            print("- Especie:", animal.getEspecie())
            print("- ID:", ID)
            print("---------------------------------")

    def infoCompletaAn(self):
        for animal in self.animales.values():
            print(f"Nombre: {animal.getNombre()}")
            print(f"Especie: {animal.getEspecie()}")
            print(f"Estado de salud: {animal.getEstadoDeSalud()}")
            print(f"Alimentación: {animal.getAliemtacion()}")
            print(f"ID: {animal.id}")
            print(f"Edad: {animal.getEdad()}")
            print(f"Temperatura máxima aceptable: {animal.getTempMaxA()}")
            print(f"Temperatura mínima aceptable: {animal.getTempMinA()}")
            print(f"Cantidad de horas dormidas: {animal.getCantHorasDormidas()}")
            print(f"Cantidad máxima de horas que puede dormir: {animal.getCantMaxDormir()}")
            print(f"Puede jugar: {animal.getJugar()}")
            print(f"Puede comer: {animal.getComer()}")
            print(f"Juguetes: {animal.juguetes}")
            print(f"Alimentos: {animal.alimentos}")
            print("\n")

    def agregarAnimal(self, animalNuevo):
        self.animales[animalNuevo.id] = animalNuevo


class HabitatAcuatico(Habitat):
    def __init__(self, nombre, tempMax, tempMin, salinidad, profundidad):
        super().__init__(nombre, tempMax, tempMin)
        self.salinidad = salinidad
        self.profundidad = profundidad


class HabitatPolar(Habitat):
    def __init__(self, nombre, tempMax, tempMin, cantidadHielo, tamanioCueva):
        super().__init__(nombre, tempMax, tempMin)
        self.cantidadHielo = cantidadHielo
        self.tamanioCueva = tamanioCueva


class HabitatDesertico(Habitat):
    def __init__(self, nombre, tempMax, tempMin, humedad, cantidadOasis):
        super().__init__(nombre, tempMax, tempMin)
        self.humedad = humedad
        self.cantidadOasis = cantidadOasis


class HabitatSelvatico(Habitat):
    def __init__(self, nombre, tempMax, tempMin, cantidadArboles, cantidadRios):
        super().__init__(nombre, tempMax, tempMin)
        self.cantidadArboles = cantidadArboles
        self.cantidadRios = cantidadRios