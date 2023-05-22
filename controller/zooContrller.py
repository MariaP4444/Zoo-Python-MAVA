import models.animal as animalModel
import models.Zoo as zooModel
import models.habitat as habitatModel
import streamlit as st
import models.Alimentacion as alimentacionModel


class zooController:
    def __init__(self, models, view):
        self.models = models
        self.view = view


    """ MENU PRINCIPAL
     Seun la opcion recibida, llama a otras funciones de las diferentes clases de los modelos y vistas y las maneja
     para llevar a cabo la accion pedida, 
    """
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

        if opcion == 3:
            self.models.listarInfoCompletaZoo()

        if opcion == 4:
            self.editarAniml()

        if opcion == 5:
            self.view.interactuar_animal()

        if opcion == 6:
            self.vincular_Animal_Habitat()

        if opcion == 7:
            self.view.informacionAPI()

    """ EDITAR ANIMAL
     Opcion: Editar animal
     Segun los atributos escogidos para cambiar utiliza funciones de la vista para pedir los datos.
     Se asegura de que los datos ingresados sean correctos y congruentes con el contexto del animal
    """
    def editarAniml(self):
        info_correcta = True
        animalModificar = self.models.listarAnimalesEnHabitat()

        options = self.view.menu_info_animal(animalModificar)

        if options:

            if "Nombre" in options:
                animalModificar.nombre = self.view.obtener_Dato_String("Nombre:")

            if "Edad" in options:
                animalModificar.edad = self.view.obtener_Dato_Int_Rango("Edad:", animalModificar.edad, 100)

            if "Estado de salud" in options:
                animalModificar.estadoDeSalud = self.view.obtener_Dato_String("Salud:")

            if "Horas de sueño" in options:
                animalModificar.cantMaxDormir = self.view.obtener_Dato_Int_Rango("Horas de sueño:", 1, 24)

            if "Cantidad de kg en dieta" in options:
                self.view.listar_alimentos_animal(animalModificar)
                i = 0
                for clave in animalModificar.alimentacion.alimentosAnimal.keys():
                    animalModificar.alimentacion.alimentosAnimal[clave] = st.slider(f"Kilogramos de {clave}:", 0, 50, 25,
                                                                           key=i + 195)
                    i += 1


            if "Agregar juguetes" in options:
                num_juguetes = self.view.obtener_Dato_Int_Rango("Numero de juguetes a agregar", 1, 15)
                if num_juguetes:
                    self.view.agregar_juguetes(animalModificar, num_juguetes, 268)

            if "Eliminar juguetes" in options:

                if len(animalModificar.juguetes) == 1:
                    self.view.mostrar_mensaje_error(f"No puedes eliminar el único juguete de {animalModificar.nombre}")
                    info_correcta = False
                else:
                    juguetes_eliminar = st.multiselect(
                        'Juguetes del animal',
                        animalModificar.juguetes)

                    if len(juguetes_eliminar) == len(animalModificar.juguetes):
                        info_correcta = False
                        self.view.mostrar_mensaje_error("No puedes eliminar todos los juguetes")
                    else:
                        for i in range(len(juguetes_eliminar)):
                            animalModificar.juguetes.remove(juguetes_eliminar[i])

            if "Agregar alimento a dieta actual" in options:
                if len(animalModificar.alimentacion.alimentosDisponibles) == 0:
                    self.view.mostrar_mensaje_error(f"No hay más alimentos disponibles dentro de la dieta de {animalModificar.nombre}")

                else:
                    alimentoNuevo = animalModificar.alimentacion.listaAlimentosDisponibles()
                    if alimentoNuevo:
                        cantKG = st.slider("Ingrese los kilogramos de" + alimentoNuevo, 0, 100)
                        if cantKG:
                            animalModificar.alimentacion.alimentosAnimal[alimentoNuevo] = cantKG

            if "Eliminar alimento en dieta actual" in options:
                if len(animalModificar.alimentacion.alimentosAnimal) == 1:
                    self.view.mostrar_mensaje_error(f"Solo hay un alimento en la dieta de {animalModificar.nombre}")
                    info_correcta = False
                else:
                    alimentoEliminar = animalModificar.alimentacion.listarAlimentosAnimal("Eliga el alimento que desea eliminar de la dieta del animal")
                    if alimentoEliminar != None:
                        animalModificar.alimentacion.eliminarAlimentoAnimal(alimentoEliminar)

            if "Agregar alimento a dieta disponible" in options:
                animalModificar.alimentacion.alimentosDisponibles.append(self.view.obtener_Dato_String("Ingrese el nombre del alimento"))

            if info_correcta:
                boton_accion = st.button("Actualizar información")
                if boton_accion:
                    self.models.buscarAnimalIdYAgregar(animalModificar.id, animalModificar)
                    st.success("La información fue actualizada correctamente")


    """ VINCULAR ANIMAL HABITAT
     Muestra los animales que no estan un habitat (registroAn) y dada la opcion escogida, presenta los habitats que cumplen con las 
     caracteristica necesarias para que albergar el animal (temperaturas, capacidad de animales, tipo de dieta).
     Dada la seleccion de habitat y animal, se vinculan ambos siendo el habitat el contenedor de animales. Al agregar el animal se
     elimina del registro que gurada los animales sin habiat
    """
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


    """ CERAR HABITAT
     Presenta los tipos de habiat para seleccionar, los tipos de alimentacion que puede tener el habitat (solo uno)
     y pide la capacidad maxima de animales del habitat. Segun el tipo de habitat escogido (selvatico, desertico, acuatico y polar)
     le asigna un rango de temperaturas pre-determinadas y le pide al usuario ingresar atributos especificos de cada tipo de habitat
    """
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


    """ CREAR ANIMAL
     Crea un objeto animal pidiendole diferentes datos al usuario, y teniendo en cuenta ciertos limites para mas congruencia, pide todos los atributos
     de la clase animal a excepcion de:
     - id: se asigna automaticamente
     - jugar: inicialmente falso
     - comer: inicialmente falso
     - cantHorasDormidas: se asume que el animal no ha dormido
     Todos los campos son obligatorios para crear el animal, se tiene que agregar al menos un juguete y un alimento
    """
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


    """ APLICAR FORMATO TABLA
     Opcion: Editar animal
     Es usada para listar los atributos basicos del animal. Dados unos datos, los agrega a una lista que sera retornada para 
     llenar una tabla
    """
    def aplicar_formato_tabla(self, animal):
        datos = []
        datos.append([animal.id, animal.nombre, animal.especie, animal.estadoDeSalud, animal.cantMaxDormir, len(animal.juguetes)])
        return datos


    """ APLICAR FORMATO TABLA
     Opcion: Editar animal
     Es usada para listar los alimentos de la diecta actual de un animal, junto con sus cantidades en kg. 
     Dados unos datos, los agrega a una lista que sera retornada para llenar una tabla
    """
    def aplicar_formato_alimentos(self, dic_alimentos):
        datos = []
        for clave in dic_alimentos.keys():
            datos.append([dic_alimentos[clave], clave])
        return datos