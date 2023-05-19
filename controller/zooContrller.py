import models.animal as animalModel
import models.Zoo as zooModel
import models.habitat as habitatModel
import streamlit as st
import models.Alimentacion as alimentacionModel


class zooController:
    def __init__(self, models, view):
        self.models = models
        self.view = view

    def menu_principalV2(self, opcion):

        if opcion == 1:
            habitat = self.crear_Habitat()
            if habitat:
                self.models.agregarAnimalRegistro(habitat)
                self.view.mostrar_mensaje_exitoso(f"Se ha agregado a {habitat.nombre} correctamente")

        if opcion == 2:
            animal = self.crear_animal(self.models.cantAnimales)
            if animal:
                self.models.cantAnimales += 1
                st.session_state["cantAnimales"] = self.models.cantAnimales
                self.view.mostrar_mensaje_exitoso(f"Se ha agregado a {animal.nombre} correctamente")
                st.balloons()

        if opcion == 4:
            id_animal = self.view.preguntar_id()
            id_habitat = self.view.obtener_Dato_Int_Rango("ID del habitat del animal:", 0)
            if id_animal and id_habitat:
                animal_temp = self.models.buscar_animal_id(id_animal, id_habitat)
                if animal_temp is None:
                    print("no existe id")
                    self.view.mostrar_mensaje_error(f"El id '{id_animal}' no corresponde a ningun animal")
                else:
                    self.view.menu_info_animal_prueba(animal_temp)
        if opcion == 5:
            print(f"edad animal 0: {self.models.registroAn[0].edad}")

    def crear_Habitat(self):
        st.divider()
        with st.container():
            st.subheader("Formulario para crear un nuevo habitat")
            tipoHabitat = self.view.seleccionar_Habitat()
            tipoAlimentacion = self.view.escoger_Alimentacion()
            cantMaxAnimales = int(self.view.obtener_Dato_Int_Rango(
                "Ingrese la cantidad maxima de animales que va poder habitat almacenar: ", 1, 50))

            if tipoHabitat == 'Selvatico':
                nuevoHabitat = habitatModel.HabitatSelvatico(tipoHabitat, 39, 20, tipoAlimentacion, cantMaxAnimales,
                                                             int(self.view.obtener_Dato_Int(
                                                                 "Ingrese la cantidad de arboles del habitat")),
                                                             int(self.view.obtener_Dato_Int(
                                                                 "Ingrese la cantidad de rios del habitat")))
            elif tipoHabitat == 'Desertico':
                nuevoHabitat = habitatModel.HabitatDesertico(tipoHabitat, 60, 40, tipoAlimentacion, cantMaxAnimales,
                                                             int(self.view.obtener_Dato_Int(
                                                                 "Ingrese el procentaje de humedad del habitat: ")),
                                                             int(self.view.obtener_Dato_Int(
                                                                 "Ingrese la cantidad de oasis del habitat")))
            elif tipoHabitat == 'Acuatico':
                nuevoHabitat = habitatModel.HabitatAcuatico(tipoHabitat, 19, 1, tipoAlimentacion, cantMaxAnimales,
                                                            int(self.view.obtener_Dato_Int(
                                                                "Ingrese el procentaje de salinidad del habitat: ")),
                                                            int(self.view.obtener_Dato_Int(
                                                                "Ingrese la profundidad del habitat")))
            else:
                nuevoHabitat = habitatModel.HabitatPolar(tipoHabitat, 0, -60, tipoAlimentacion, cantMaxAnimales,int(self.view.obtener_Dato_Int(
                                                                "Ingrese el procentaje de hielo del habitat: ")),
                                                            int(self.view.obtener_Dato_Int(
                                                                "Ingrese el tamaño de las cuevas del habitat")))
            if tipoHabitat and tipoAlimentacion and cantMaxAnimales:
                boton_accion = st.button("Crear nuevo habitat")
                if boton_accion:
                    return nuevoHabitat
            else:
                st.error("Faltan datos")

    def menu_cambiar_infoAn(self, opcion, animal):
        if opcion == 1:
            edad = self.view.edad_animal()
            animal.edad = edad
            # self.view.mostrar_mensaje_exitoso(f"Se ha actualizado la edad a {edad} anios")
        if opcion == 2:
            salud = self.view.pedir_salud()
            animal.estadoDeSalud = salud
            # self.view.mostrar_mensaje_exitoso(f"Se ha actualizado la edad a {edad} anios")

        # edad = self.models.animal.edad
        # salud = self.models.animal.estadoDeSalud

    def crear_animal(self, id):
        st.divider()
        with st.container():
            st.subheader("Formulario para crear un nuevo producto")
            nuevoAnimal = animalModel.Animal()
            nuevoAnimal.nombre = self.view.obtener_Dato_String("Ingrese el nombre del animal:")
            nuevoAnimal.especie = self.view.obtener_Dato_String("Ingrese la especie del animal:")
            nuevoAnimal.estadoDeSalud = self.view.obtener_Dato_String("Ingrese el estado de salud del animal:")
            nuevoAnimal.id = id


            nuevoAnimal.edad = self.view.obtener_Dato_Int_Rango("Ingrese la edad del animal La edad debe ser un entero "
                                                                "positivo menor o igual a 100", 0, 100)

            nuevoAnimal.tempMaxA = self.view.obtener_Dato_Int("Ingrese la temperatura maxima: ")

            nuevoAnimal.tempMinA = st.number_input("Ingrese la temperatura minima del animal: ",
                                                   max_value=nuevoAnimal.tempMaxA)

            cantJuguetes = self.view.obtener_Dato_Int_Rango("Ingrese el número de juguetes que va a tener el animal:",
                                                            1, 15)

            lista_juguetes = []
            if cantJuguetes:
                col1, col2 = st.columns([3, 1])
                i = 1
                while i <= cantJuguetes:
                    with st.container():
                        nombre = col1.text_input(f"Nombre juguete {i}:", key=i + 95)
                        print(i)
                        lista_juguetes.append(nombre)
                    i += 1
            nuevoAnimal.juguetes = lista_juguetes

            nuevoAnimal.alimentacion = alimentacionModel.Alimentacion()
            nuevoAnimal.alimentacion.tipoDieta = self.view.escoger_Alimentacion()
            nuevoAnimal.alimentacion.designadorDeAlimentosDispo()
            x = len(nuevoAnimal.alimentacion.alimentosDisponibles)
            st.caption(
                f"Segun el tipo de dieta:blue[{nuevoAnimal.alimentacion.tipoDieta}], este puede comer hasta:blue[{x}] distintos tipos de alimentos")

            options = st.multiselect(
                'Alimentos diponibles para el animal',
                nuevoAnimal.alimentacion.alimentosDisponibles)



            kgs = []
            if options:
                col1, col2 = st.columns([3, 1])
                i = 0
                while i < len(options):
                    with st.container():
                        print(i)
                        kg = st.slider(f"Kilogramos de {options[i]}:", 0, 100, 25, key=i + 155, )
                        print(i)
                        kgs.append(kg)
                    i += 1

            alimentos = {}
            for clave in range(len(options)):
                alimentos[kgs[clave]] = options[clave]

            nuevoAnimal.alimentacion.alimentosAnimal = alimentos

            self.models.agregarAnimalRegistro(nuevoAnimal)

            if nuevoAnimal.nombre and nuevoAnimal.tempMaxA and nuevoAnimal.alimentacion and nuevoAnimal.juguetes:
                boton_accion = st.button("Crear nuevo animal")
                if boton_accion:
                    return nuevoAnimal
            else:
                st.error("Faltan datos")