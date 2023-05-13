

class Zoo:
    def __init__(self):
        self.nombre = "ZooMAVA"
        self.cantAnimales = 0
        self.zooNoVacio = False
        self.habitats = []
        self.registroAn = {}
        self.dietaCarnivora = []
        self.dietaHerbivora = []

    def existeHabitatTemp(self, temMax, temMin):
        for habitat in self.habitats:
            if habitat.getTempMax() <= temMax and habitat.getTempMin() >= temMin:
                return True
        return False

    def lista_dietas_disponibles(self, tipoDieta):
        dietasDispo = ["carnivoro", "herbivoro", "omnivoro"]

        if tipoDieta in dietasDispo:
            return True
        else:
            return False

    def buscar_animal_id(self, id):
        for clave, animal in self.registroAn.items():
            if clave == id:
                return animal
            else:
                return None