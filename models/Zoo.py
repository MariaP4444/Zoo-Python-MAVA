import streamlit as st
import models.habitat as habitatModel

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


    """ ELIMINAR ANIMAL REGISTRO
     Opcion: Vincular animal
     Dado un ID se elimina un animal del registro que guarda animales sin habitat
    """
    def eliminarAnimalRegistro(self, id):
        self.registroAn.pop(id)


    """ AGREGAR ANIMAL REGISTRO
     Agrega al diccionario registroAn de Zoo un animal nuevo como valor con su ID como clave
    """
    def agregarAnimalRegistro(self, animalNuevo):
        self.registroAn[animalNuevo.id] = animalNuevo


    """ AGREGAR HABITAT
     Opcion: Crear habitat
     Agrega a la lista habitats de Zoo un objeto habitat
    """
    def agregarHabitat(self, habitat):
        self.habitats.append(habitat)


    """ LISTAR ANIMALES REGISTRO
     Opcion: Vincular animal con habitat
     Muestra como opciones los diferentes animales que no tienen habitat, mostrando la siguiente informacion
     - ID
     - nombre
     - dieta
     Devuelve el animal escogido a la funcion vincular_Animal_Habitat para luego hacer un posible vinculo
    """
    def listarAnimalesRegistro(self):
        listaInfoBasicaAnimal = []
        listaId = []

        for id in self.registroAn:
            texto = "++ Id:" + str(id) + " ++ " + "Nombre: " + self.registroAn[id].nombre+ " ++ " + "dieta: " + self.registroAn[id].alimentacion.tipoDieta
            listaId.append(id)
            listaInfoBasicaAnimal.append(texto)

        opcion = st.radio(
            "Escoge el animal que deseas vincular con un habitat",
            listaInfoBasicaAnimal)

        if opcion:
            animalAgregar = self.registroAn[listaId[listaInfoBasicaAnimal.index((opcion))]]
            return animalAgregar

    """ LISTAR HABITATS DISPONIBLES
     Opcion: Vincular animal con habitat
     Segun el aninal dado, saca un listado de habitats de la lista de habitats de ZOO que cumplen con las siguientes condiciones:
     - Que no haya sobrepasado la cantidad maxima de alimentos
     - Que el rango de temperaturas del animal este dentro o sea igual al rango de temperaturas del habitat
     - Que el tipo de alimentacion del habitat y el animal coincidan
     De haber algun habitat que las cumpla, el usuario escoge una y esta es retornada para hacer el vinculo. En el caso contrario, retorna None.
    """
    def listarHabitatasDiponiblesAnimal(self, animal):
        habitatsDisponibles = []
        listaIndices = []
        indice = 0
        for habitat in self.habitats:
            if habitat.dieta == animal.alimentacion.tipoDieta and (
            len(habitat.animales)) + 1 <= habitat.cantMaxAnimales and habitat.tempMin <= animal.tempMinA and habitat.tempMax >= animal.tempMaxA:
                texto = habitat.nombre
                habitatsDisponibles.append(texto)
                listaIndices.append(indice)
            indice += 1

        opcion = st.radio(
            "Escoge el habitat que deseas vincular con un animal",
            habitatsDisponibles)

        if opcion:
            st.write(listaIndices[habitatsDisponibles.index((opcion))])
            habitat = self.habitats[listaIndices[habitatsDisponibles.index((opcion))]]
            return habitat
        else:
            return None


    """ BUSCAR ANIMAL ID Y AGREGAR
     Opcion: Crear habitat
     Busca en los animales de todos los habitats y en el registro con el ID del animal para asignarle el animal que ha sido modificado
    """
    def buscarAnimalIdYAgregar(self, id,animalModificado):

        for habitat in self.habitats:
            for ID, animal in habitat.animales.items():
                if ID == id:
                    habitat.animales[id] = animalModificado

        for ID_R in self.registroAn:
            if ID_R == id:
                self.agregarAnimalRegistro(animalModificado)


    """ LISTAR ANIMALES EN HABITAT
     Lista los animales de todos los habitats y los animales que no tienen habitat. Los da como opciones para que el usuario escoja uno
     y devuelve el animal escogido. Se usa para las opciones 4 y 5 para escoger uno para luego editarlo o interactuar con el
    """
    def listarAnimalesEnHabitat(self):
        opciones = []
        for habitat in self.habitats:
            for ID, animal in habitat.animales.items():
                texto = "++ Id:" + str(ID) + " ++ " + "Nombre: " +habitat.animales[ID].nombre + " ++ " + "dieta: " + \
                        habitat.animales[ID].alimentacion.tipoDieta
                opciones.append(texto)

        for id in self.registroAn:
            texto = texto = "++ Id:" + str(id) + " ++ " + "Nombre: " + self.registroAn[id].nombre+ " ++ " + "dieta: " + self.registroAn[id].alimentacion.tipoDieta
            opciones.append(texto)

        opcion = st.selectbox(
            "Escoje un animal",
            opciones)

        if opcion:
            # Lo busca en los habitats
            for habitat in self.habitats:
                for ID, animal in habitat.animales.items():
                    if "++ Id:" + str(ID) + " ++ " + "Nombre: " + habitat.animales[ID].nombre + " ++ " + "dieta: " + habitat.animales[ID].alimentacion.tipoDieta == opcion:
                        return habitat.animales[ID]

            # Lo busca en el registro
            for id in self.registroAn:
                if "++ Id:" + str(id) + " ++ " + "Nombre: " + self.registroAn[id].nombre + " ++ " + "dieta: " + self.registroAn[id].alimentacion.tipoDieta == opcion:
                    return self.registroAn[id]

        else:
            return None

    """ LISTAR INFO COMPLETA ZOO
     Opcion: Listar animales
     Enseña a traves de un desplegable los animales que estan en el registro (no tienen habitat) con su respectiva informacio.
     De igual manera enseña la información de cada uno de los habitats y la informacion de sus respectivos animales
    """
    def listarInfoCompletaZoo(self):
        st.divider()

        if len(self.registroAn) == 0 and len(self.habitats) == 0:
            st.subheader("No hay nada de informacion en el Zoo")
        else:
            with st.expander("Registro:"):
                if (len(self.registroAn) == 0):
                    st.subheader("No hay hay animales en el registro")
                else:
                    for id in self.registroAn:
                        st.subheader(":blue[Animales]")
                        st.subheader(self.registroAn[id].nombre)
                        st.write(" - ID: ", id)
                        st.write(" - Especie: ", self.registroAn[id].especie)
                        st.write(" - Edad: ", self.registroAn[id].edad)
                        st.write(" - Estado de salud: ", self.registroAn[id].estadoDeSalud)
                        st.write(" - Temperatura maxima:", self.registroAn[id].tempMaxA)
                        st.write(" - Temperatura minima:", self.registroAn[id].tempMinA)
                        st.write(" - Cantidad de horas dormidas:", self.registroAn[id].cantHorasDormidas)
                        st.write(" - Alimentacion: ", self.registroAn[id].alimentacion.tipoDieta)
                        self.registroAn[id].alimentacion.imprimirListaAlimentosAnimal()
                        st.write(" - Juguetes: ")
                        self.registroAn[id].imprimirJuguetes()
                        st.divider()

            for habitat in self.habitats:
                with st.expander(habitat.nombre):
                    st.subheader(":blue[Informacion habitat]")
                    st.write(" - Tipo de habitat: ", habitat.nombre)
                    st.write(" - Temperatura maxima:", habitat.tempMax)
                    st.write(" - Temperatura minima:", habitat.tempMin)
                    st.write(" - Cantidad Maxima Animales: ", habitat.cantMaxAnimales)
                    st.write(" - Dieta: ", habitat.dieta)
                    if (len(habitat.animales) == 0):
                        st.subheader("- No hay hay animales en el habitat -")
                    else:
                        for ID, animal in habitat.animales.items():
                            st.subheader(":blue[Animales]")
                            st.subheader(self.registroAn[id].nombre)
                            st.write(" - ID: ", ID)
                            st.write(" - Especie: ", animal.especie)
                            st.write(" - Edad: ", animal.edad)
                            st.write(" - Estado de salud: ", animal.estadoDeSalud)
                            st.write(" - Temperatura maxima:", animal.tempMaxA)
                            st.write(" - Temperatura minima:", animal.tempMinA)
                            st.write(" - Cantidad de horas dormidas:", animal.cantHorasDormidas)
                            st.write(" - Alimentacion: ", animal.alimentacion.tipoDieta)
                            animal.alimentacion.imprimirListaAlimentosAnimal()
                            st.write(" - Juguetes: ")
                            animal.imprimirJuguetes()
                            st.divider()