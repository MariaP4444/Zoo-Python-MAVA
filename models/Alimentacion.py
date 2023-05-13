class Alimentacion:
    def __init__(self, tipoDieta,alimentosDisponibles = [], alimentosAnimal= {}):
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

    def elegirAlim(self,cantidadAlimeto1,cantidadAlimeto2,cantidadAlimeto3):
        if self.tipoDieta == "carnivoro":
            self.alimentosAnimal["res"] = cantidadAlimeto1
            self.alimentosAnimal["pollo"] = cantidadAlimeto2
            self.alimentosAnimal["pescado"] = cantidadAlimeto3
            self.alimentosDisponibles = ["viseras", "gambas", "almejas", "huevos", "cerdo", "pollo", "res", "pescado"]

        elif self.tipoDieta == "herbivoro":
            self.alimentosAnimal["frutas"] = cantidadAlimeto1
            self.alimentosAnimal["verduras"] = cantidadAlimeto2
            self.alimentosAnimal["granos"] = cantidadAlimeto3
            self.alimentosDisponibles = ["semillas", "granos", "verduras", "frutas", "polen", "nectar", "flores", "savia", "corteza", "hojas","raices"]


        elif self.tipoDieta == "omnivoro":
            self.alimentosAnimal["res"] = cantidadAlimeto1
            self.alimentosAnimal["pollo"] = cantidadAlimeto2
            self.alimentosAnimal["frutas"] = cantidadAlimeto3
            self.alimentosDisponibles = ["viseras", "gambas", "almejas", "huevos", "cerdo", "pollo", "res", "pescado","semillas", "granos", "verduras", "frutas", "polen", "nectar", "flores", "savia", "corteza", "hojas","raices"]

