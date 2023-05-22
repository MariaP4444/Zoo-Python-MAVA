import streamlit as st

class Alimentacion:
    def __init__(self, tipoDieta = '',alimentosDisponibles = [], alimentosAnimal= {}):
        self.tipoDieta = tipoDieta
        self.alimentosDisponibles = alimentosDisponibles
        self.alimentosAnimal = alimentosAnimal


    """ ELIMINAR ALIMENTO ANIMAL
     Opcion = Editar animal
     Dado un alimento, lo elimina del diccionario de la dieta actual del animal
    """
    def eliminarAlimentoAnimal(self, alimentoEliminar):
        self.alimentosAnimal.pop(alimentoEliminar)


    """ DESIGNADOR DE ALIMENTOS DISPONIBLES
     Opcion: Agregar animal
     Segun el tipo de dieta que se designo para un animal al momento de crearlo, se agrega una lista de 
     alimentos para cada tipo de dieta. Las cuales se pueden añadir a la dieta actual del animal. Esta lista se puede expandir
     o reducir en la opcion editar animal. No se puede agregar un alimento a la dieta actual del animal sin que este en la diesta disponible
    """
    def designadorDeAlimentosDispo(self):
        if self.tipoDieta == "carnivora":
            self.alimentosDisponibles = ["viseras", "gambas", "almejas", "huevos", "cerdo", "pollo", "res", "pescado"]

        elif self.tipoDieta == "herbivora":
            self.alimentosDisponibles = ["semillas", "granos", "verduras", "frutas", "polen", "nectar", "flore",
                                         "savia", "corteza", "hojas", "raices"]

        elif self.tipoDieta == "omnivora":
            self.alimentosDisponibles = ["viseras", "gambas", "almejas", "huevos", "cerdo", "pollo", "res", "pescado",
                                         "semillas", "granos", "verduras", "frutas", "polen", "nectar", "flores",
                                         "savia", "corteza", "hojas", "raices"]


    """ LISTA ALIMENTOS DISPONIBLES
     Opcion: Editar animal
     Muestra como opciones los diferentes alimentos que se pueden añadir a la dieta actual del animal.
     Al seleccionar uno, lo retorna a la funcion editar animal para que el usuario defina la cantidad de kg 
     y se le agreque a la dieta actual
    """
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


    """ LISTAR ALIMENTOS ANIMAL
     Opcion: Editar animal
     Muestra como opciones los diferentes alimentos que se pueden eliminar de la dieta actual del animal.
     Al seleccionar uno, lo retorna a la funcion editar animal para que se elimine
    """
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


    """ IMPRIMIR LISTA ALIMENTOS ANIMAL
     Opcion: Listar animales
     Se usa para mostrar cada alimento con su cantidad de kg de la dieta actual de un animal
    """
    def imprimirListaAlimentosAnimal(self):
        for alimento, cantidad in self.alimentosAnimal.items():
            st.write("")
            st.write("    -- Alimento: ", alimento)
            st.write("    -- Cantidad en kg: ", cantidad)
            st.write("")
