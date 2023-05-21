import streamlit as st

class Zoo:
    def __init__(self):
        if "registroAn":
            if "registroAn" in st.session_state:
                self.registroAn = st.session_state["registroAn"]
            else:
                self.registroAn = {}
                st.session_state["registroAn"] = {}

        self.nombre = "ZooMAVA"

        if "cantAnimales":
            if "cantAnimales" in st.session_state:
                self.cantAnimales = st.session_state["cantAnimales"]
            else:
                self.cantAnimales = 1
                st.session_state["cantAnimales"] = 1

        if "habitats":
            if "habitats" in st.session_state:
                self.habitats = st.session_state["habitats"]
            else:
                self.habitats = []
                st.session_state["habitats"] = []

    def eliminarAnimalRegistro(self,id):
        self.registroAn.pop(id)

    def existeHabitatTemp(self, temMax, temMin):
        for habitat in self.habitats:
            if habitat.getTempMax() <= temMax and habitat.getTempMin() >= temMin:
                return True
        return False

    def buscar_animal_id(self, id_animal, id_habitat):

        for clave, animal in self.registroAn.items():
            if clave == id:
                return animal

        for clave, animal in self.habitats[id_habitat].animales.items():
            if clave == id_animal:
                return animal
        return None

    def agregarAnimalRegistro(self, animalNuevo):
        self.registroAn[animalNuevo.id] = animalNuevo

    def agregarHabitat(self, habitat):
        self.habitats.append(habitat)

    def listarAnimalesRegistro(self):
        listaInfoBasicaAnimal = []
        listaId = []

        for id in self.registroAn:
            texto = "++ Id:" + str(id) + " ++ " + "Nombre: " + self.registroAn[id].nombre + "dieta: " + self.registroAn[id].alimentacion.tipoDieta
            listaId.append(id)
            listaInfoBasicaAnimal.append(texto)

        opcion = st.radio(
            "Escoge el animal que deseas vincular con un animal",
            listaInfoBasicaAnimal)

        if opcion:
            animalAgregar= self.registroAn[listaId[listaInfoBasicaAnimal.index((opcion))]]
            return animalAgregar

    def listarHabitatasDiponiblesAnimal(self, animal):
        habitatsDisponibles = []
        listaIndices = []
        indice = 0
        for habitat in self.habitats:
            if habitat.dieta == animal.alimentacion.tipoDieta and (len(habitat.animales)) + 1 <= habitat.cantMaxAnimales and habitat.tempMin<= animal.tempMinA and habitat.tempMax >= animal.tempMaxA:
                texto = habitat.nombre
                habitatsDisponibles.append(texto)
                listaIndices.append(indice)
            indice+=1

        opcion = st.radio(
            "Escoge el animal que deseas vincular con un animal",
            habitatsDisponibles)

        if opcion:
            st.write(listaIndices[habitatsDisponibles.index((opcion))])
            habitat = self.habitats[listaIndices[habitatsDisponibles.index((opcion))]]
            return habitat
        else:
            return None

