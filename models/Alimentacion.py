class Alimentacion:
    def __init__(self, tipoDieta = '',alimentosDisponibles = [], alimentosAnimal= {}):
        self.tipoDieta = tipoDieta
        self.alimentosDisponibles = alimentosDisponibles
        self.alimentosAnimal = alimentosAnimal


    def agregarAlimentoDisponible(self, alimentoNuevo):
        self.alimentosDisponibles.append(alimentoNuevo)

    def agregarAlimentoAnimal(self, alimentoNuevo):
        self.alimentosAnimal.append(alimentoNuevo)

    def eliminarAlimentoDisponible(self, alimentoEliminar):
        self.alimentosDisponibles.remove(alimentoEliminar)

    def eliminarAlimentoAnimal(self, alimentoEliminar):
        self.alimentosAnimal.remove(alimentoEliminar)

    def designadorDeAlimentosDispo(self):
        print(f"dieta actual = {self.tipoDieta}")
        if self.tipoDieta == "carnivora":
            print("c")
            self.alimentosDisponibles = ["viseras", "gambas", "almejas", "huevos", "cerdo", "pollo", "res", "pescado"]

        elif self.tipoDieta == "herbivora":
            print("h")
            self.alimentosDisponibles = ["semillas", "granos", "verduras", "frutas", "polen", "nectar", "flore",
                                         "savia", "corteza", "hojas", "raices"]

        elif self.tipoDieta == "omnivora":
            print("o")
            self.alimentosDisponibles = ["viseras", "gambas", "almejas", "huevos", "cerdo", "pollo", "res", "pescado",
                                         "semillas", "granos", "verduras", "frutas", "polen", "nectar", "flores",
                                         "savia", "corteza", "hojas", "raices"]

