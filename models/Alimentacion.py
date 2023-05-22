import streamlit as st

class Alimentacion:
    def __init__(self, tipoDieta = '',alimentosDisponibles = [], alimentosAnimal= {}):
        self.tipoDieta = tipoDieta
        self.alimentosDisponibles = alimentosDisponibles
        self.alimentosAnimal = alimentosAnimal

    def eliminarAlimentoAnimal(self, alimentoEliminar):
        self.alimentosAnimal.pop(alimentoEliminar)

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

    def listaAlimentosDisponibles(self):
        listaAlimentosPosibles = []

        for alimentoPosible in self.alimentosDisponibles:
            listaAlimentosPosibles.append(alimentoPosible)

        seleccionar_alimento_posible = st.selectbox(
            "Escoge el alimento que le vas a agregar a la dieta actual del animal",
            listaAlimentosPosibles)

        if seleccionar_alimento_posible:
            return seleccionar_alimento_posible
        else:
            return None

    def listarAlimentosAnimal(self, mensaje):
        listaAlimentos = [""]

        for alimento in self.alimentosAnimal:
            listaAlimentos.append(alimento)

        seleccionar_alimento = st.selectbox(
            mensaje,
            listaAlimentos, key="listaAlimentosActuales")

        if seleccionar_alimento != "":
                return seleccionar_alimento
        else:
            return None

    def imprimirListaAlimentosAnimal(self):
        for alimento, cantidad in self.alimentosAnimal.items():
            st.write("")
            st.write("    -- Alimento: ", alimento)
            st.write("    -- Cantidad en kg: ", cantidad)
            st.write("")
