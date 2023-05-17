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
