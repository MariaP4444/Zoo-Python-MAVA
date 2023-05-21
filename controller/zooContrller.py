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
                self.models.agregarHabitat(habitat)
                self.view.mostrar_mensaje_exitoso(f"Se ha agregado a {habitat.nombre} correctamente")

        if opcion == 2:
            animal = self.crear_animal(self.models.cantAnimales)
            if animal:
                self.models.agregarAnimalRegistro(animal)
                self.models.cantAnimales += 1
                st.session_state["cantAnimales"] = self.models.cantAnimales
                self.view.mostrar_mensaje_exitoso(f"Se ha agregado a {animal.nombre} correctamente")
                st.balloons()

        if opcion == 4:
            self.buscar_id(4)

        if opcion == 5:
            self.buscar_id(5)

        if opcion == 6:

            self.vincular_Animal_Habitat()

    def buscar_id(self, opc):

        if self.models.cantAnimales == 0:
            self.view.mostrar_mensaje_error("No hay animales")

        else:
            id_animal = self.view.preguntar_id()

            if id_animal:

                if id_animal > self.models.cantAnimales:
                    self.view.mostrar_mensaje_error("No existe ID del habitat")
                else:
                    if id_animal not in self.models.registroAn:
                        id_habitat = self.view.obtener_Dato_Int_Rango("ID del habitat del animal:", 0)

                        if id_habitat:

                            if id_habitat not in self.models.habitats:
                                self.view.mostrar_mensaje_error("No existe ID del habitat")
                            else:
                                animal = self.models.habitats[id_habitat].animales[id_animal]
                                if opc == 4:
                                    self.view.menu_info_animal_prueba(animal)
                                    #Retorna 1 porque las opciones 4 y 5 usan esta función
                                    return 1
                                elif opc == 5:
                                    self.view.escoger_actividad(animal)
                                    return 1
                    else:
                        animal = self.models.registroAn[id_animal]
                        if opc == 4:
                            self.view.menu_info_animal_prueba(animal)
                            return 1
                        elif opc == 5:
                            self.view.escoger_actividad(animal)
                            return 1


    def vincular_Animal_Habitat(self):
        st.divider()
        if len(self.view.zoo.registroAn) >= 1:
            animalAgregar = self.models.listarAnimalesRegistro()
            st.write('animal', animalAgregar.id)
            if len(self.view.zoo.habitats) >= 1:
                habitat = self.models.listarHabitatasDiponiblesAnimal(animalAgregar)
                if habitat == None:
                    st.write('NO hay habitat para el animal')
                else:
                    st.write('habitat', habitat.nombre, "DIETA ", habitat.dieta)
                    boton_agregar = st.button("Agregar el animal al habitat")
                    if boton_agregar:
                        if habitat:
                            habitat.agregarAnimal(animalAgregar)
                            self.models.eliminarAnimalRegistro(animalAgregar.id)
                            self.view.mostrar_mensaje_exitoso("El animal fue agregado al habitat correctamente")
                        else:
                            self.view.mensajeError("No has seleccionado a ningun habitat para agregar al animal")
            else:
                st.write('NO hay habitat para el animal')

        else:
            st.write("No hay animales por el moemento en el registro")

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



    def crear_animal(self, id):
        st.divider()
        with st.container():
            st.subheader("Formulario para crear un nuevo producto")
            nuevoAnimal = animalModel.Animal()

            nuevoAnimal.comer = False
            nuevoAnimal.cantHorasDormidas = 0
            nuevoAnimal.jugar = False

            nuevoAnimal.nombre = self.view.obtener_Dato_String("Ingrese el nombre del animal:")
            nuevoAnimal.especie = self.view.obtener_Dato_String("Ingrese la especie del animal:")
            nuevoAnimal.estadoDeSalud = self.view.obtener_Dato_String("Ingrese el estado de salud del animal:")
            nuevoAnimal.id = id


            nuevoAnimal.edad = self.view.obtener_Dato_Int_Rango("Ingrese la edad del animal La edad debe ser un entero "
                                                                "positivo menor o igual a 100", 0, 100)

            nuevoAnimal.tempMaxA = st.slider("Ingrese la temperatura maxima del animal: ", -59, 60)

            nuevoAnimal.tempMinA = st.slider("Ingrese la temperatura maxima del animal: ", -60,nuevoAnimal.tempMaxA)

            nuevoAnimal.cantMaxDormir = self.view.obtener_Dato_Int_Rango("Ingrese el numero de horas diarias de sueño",
                                                                         1, 24)

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

            seleccion_alimentos = st.multiselect(
                'Alimentos diponibles para el animal',
                nuevoAnimal.alimentacion.alimentosDisponibles)


            kgs = []
            if seleccion_alimentos:
                col1, col2 = st.columns([3, 1])
                i = 0
                while i < len(seleccion_alimentos):
                    with st.container():
                        print(i)
                        kg = st.slider(f"Kilogramos de {seleccion_alimentos[i]}:", 0, 100, 25, key=i + 155, )
                        print(i)
                        kgs.append(kg)
                    i += 1

            alimentos = {}
            for clave in range(len(seleccion_alimentos)):
                alimentos[seleccion_alimentos[clave]] = kgs[clave]

            nuevoAnimal.alimentacion.alimentosAnimal = alimentos

            if nuevoAnimal.nombre and nuevoAnimal.tempMaxA and nuevoAnimal.alimentacion and nuevoAnimal.juguetes:
                boton_accion = st.button("Crear nuevo animal")
                if boton_accion:
                    return nuevoAnimal
            else:
                st.error("Faltan datos")


    def aplicar_formato_tabla(self, animal):
        datos = []
        datos.append([animal.id, animal.nombre, animal.especie, animal.estadoDeSalud, animal.cantMaxDormir, len(animal.juguetes)])
        return datos

    def aplicar_formato_alimentos(self, dic_alimentos):
        datos = []
        for clave in dic_alimentos.keys():
            print(f"clave:{clave}")
            datos.append([dic_alimentos[clave], clave])
        return datos