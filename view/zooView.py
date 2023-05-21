import models.Zoo as zooModel
import streamlit as st
import controller.zooContrller as zooController
import pandas as pd


class zooView:
    def __init__(self):
        self.zoo = zooModel.Zoo()
        self.controlador = zooController.zooController(self.zoo, self)


    def prueba(self):
        opcion = 0

        st.title("Bienvenido el zoologico MAVA")

        with st.container():
            col1, col2, col3, col4, col5, col6 = st.columns(6)
            boton_agregar_habitat = col1.button("Agregar habitat", 1)
            boton_agregar_animal = col2.button("Agregar animal", 2)
            boton_listar_habitats = col3.button("Listar animales", 3)
            boton_modificar_infoAn = col4.button("Editar animal", 4)
            boton_visitar_habitat = col5.button("Interactuar con animal", 5)
            boton_vincular_Animal_Habitat = col6.button("Vincular animal con un habitat",6)

        if boton_agregar_habitat:
            st.session_state["opcion"] = 1
        elif boton_agregar_animal:
            st.session_state["opcion"] = 2
        elif boton_listar_habitats:
            st.session_state["opcion"] = 3
        elif boton_modificar_infoAn:
            st.session_state["opcion"] = 4
        elif boton_visitar_habitat:
            st.session_state["opcion"] = 5
        elif boton_vincular_Animal_Habitat:
            st.session_state["opcion"] = 6

        if "opcion" in st.session_state:
            self.controlador.menu_principalV2(st.session_state["opcion"])


    def seleccionar_Habitat(self):
        opcion = st.radio(
            "Escoge el tipo de habitat que vas a crear:",
            ('Selvatico', 'Desertico', 'Acuatico','Polar'))

        if opcion == 'Selvatico':
            st.write('El habitat selvatico tiene una temperatura de (20 a 39 grados)')
        elif opcion == 'Desertico':
            st.write('El habitat desertico tiene una temperatura de (40 a 60 grados)')
        elif opcion == 'Acuatico':
            st.write('El habitat acuatico tiene una temperatura de (1 a 19 grados)')
        else:
            st.write('El habitat polar tiene una temperatura de (0 a -60 grados)')


        return opcion



    def preguntar_id(self):
        id = st.number_input("Ingrese el id del animal: ", min_value=0)
        return id


    def escoger_actividad(self, animal):

        actividades = ['comer', 'dormir', 'jugar']

        option = st.selectbox(
            'Tipo de dieta',
            actividades)

        if option:

            if option == "comer":
                print(f"comer = {animal.comer}")
                if animal.comer:
                    self.mostrar_mensaje_error(f"{animal.nombre} ya ha comido el día de hoy")
                else:
                    alimento = st.selectbox(
                        'Escoge un alimento',
                        animal.alimentacion.alimentosAnimal)

                    if alimento:
                        boton_accion = st.button("Dar de comer")

                        if boton_accion:
                            self.mostrar_mensaje_exitoso(f"{animal.nombre} está comiendo {animal.alimentacion.alimentosAnimal[alimento]} kg de {alimento}")
                            animal.comer = True

            elif option == "dormir":
                if animal.cantHorasDormidas == animal.cantMaxDormir:
                    self.mostrar_mensaje_error(f"{animal.nombre} ya ha dormido suficiente el día de hoy")
                else:
                    hSuenio = self.obtener_Dato_Int_Rango("Ingrese las horas que va a dormir", 1, animal.cantMaxDormir - animal.cantHorasDormidas)

                    if hSuenio:
                        boton_accion = st.button("Mandar a dormir")

                        if boton_accion:
                            self.mostrar_mensaje_exitoso(
                                f"{animal.nombre} va a dormir durante  {hSuenio} horas")
                            animal.cantHorasDormidas += hSuenio


            elif option == "jugar":
                if animal.jugar:
                    self.mostrar_mensaje_error(f"{animal.nombre} ya ha jugado el día de hoy")
                else:
                    juguete = st.selectbox(
                        'Escoge un juguete',
                        animal.juguetes)

                    if juguete:
                        boton_accion = st.button("Mandar a jugar")

                        if boton_accion:
                            self.mostrar_mensaje_exitoso(
                                f"{animal.nombre} está jugando con su {juguete}")
                            animal.jugar = True

    def menu_info_animal_prueba(self, animal):

        info_correcta = True
        self.listar_atributos_animal(animal)
        datos_cambiar = ['Nombre', 'Edad', 'Estado de salud', 'Horas de sueño', 'Cantidad de kg en dieta', 'Agregar juguetes', 'Eliminar juguetes', 'Agregar alimento a dieta actual', 'Eliminar alimento en dieta actual', 'Agregar alimento a dieta disponible']


        options = st.multiselect(
            'Elige los datos a editar',
            datos_cambiar)

        if options:

            if "Nombre" in options:
                animal.nombre = self.obtener_Dato_String("Nombre:")

            if "Edad" in options:
                animal.edad = self.obtener_Dato_Int_Rango("Edad:", animal.edad, 100)

            if "Estado de salud" in options:
                animal.estadoDeSalud= self.obtener_Dato_String("Salud:")

            if "Horas de sueño" in options:
                animal.cantMaxDormir = self.obtener_Dato_Int_Rango("Horas de sueño:", 1, 24)

            if "Cantidad de kg en dieta" in options:

                self.listar_alimentos_animal(animal)
                i = 0
                for clave in animal.alimentacion.alimentosAnimal.keys():
                    animal.alimentacion.alimentosAnimal[clave] = st.slider(f"Kilogramos de {clave}:", 0, 50, 25, key=i + 195)
                    i+=1

            if "Agregar juguetes" in options:

                num_juguetes = self.obtener_Dato_Int_Rango("Numero de juguetes a agregar", 1, 15)
                if num_juguetes:
                    self.agregar_juguetes(animal, num_juguetes, 268)

            if "Eliminar juguetes" in options:

                if len(animal.juguetes) == 1:
                    self.mostrar_mensaje_error(f"No puedes eliminar el único juguete de {animal.nombre}")
                else:
                    juguetes_eliminar = st.multiselect(
                        'Juguetes del animal',
                        animal.juguetes)

                    if len(juguetes_eliminar) == len(animal.juguetes):
                        info_correcta = False
                        self.mostrar_mensaje_error("No puedes eliminar todos los juguetes")
                    else:
                        for i in range(len(juguetes_eliminar)):
                            animal.juguetes.remove(juguetes_eliminar[i])


            if "Agregar alimento a dieta actual" in options:

                if len(animal.alimentacion.alimentosDisponibles) == 0:
                    self.mostrar_mensaje_error(f"No hay más alimentos disponibles dentro de la dieta de {animal.nombre}")

                else:

                    alimentos_agregar = st.multiselect(
                        'Alimentos diponibles para el animal',
                        animal.alimentacion.alimentosDisponibles)

                    if alimentos_agregar:
                        kgs = []
                        col1, col2 = st.columns([3, 1])
                        i = 0
                        while i < len(alimentos_agregar):
                            with st.container():
                                kg = st.slider(f"Kilogramos de {alimentos_agregar[i]}:", 0, 50, 25, key=i + 238)
                                print(i)
                                kgs.append(kg)
                            i += 1

                        for clave in range(len(alimentos_agregar)):
                            animal.alimentacion.alimentosAnimal[alimentos_agregar[clave]] = kgs[clave]


            if "Eliminar alimento en dieta actual" in options:

                if len(animal.alimentacion.alimentosAnimal) == 1:
                    self.mostrar_mensaje_error(f"No puedes eliminar el único alimento de {animal.nombre}")

                else:
                    alimentos_eliminar = st.multiselect(
                        'Alimentos de la dieta del animal',
                        animal.alimentacion.alimentosAnimal)

                    if alimentos_eliminar:

                        if len(alimentos_eliminar) == len(animal.alimentacion.alimentosAnimal):
                            info_correcta = False
                            self.mostrar_mensaje_error("No puedes eliminar todos los alimentos")
                        else:
                            for i in range(len(alimentos_eliminar)):
                                del animal.alimentacion.alimentosAnimal[alimentos_eliminar[i]]


            if "Agregar alimento a dieta disponible" in options:
                animal.alimentacion.alimentosDisponibles.append(self.obtener_Dato_String("Ingrese el nombre del alimento"))

            if info_correcta:
                boton_accion = st.button("Actualizar información")

                if boton_accion:
                    if "Agregar alimento a dieta actual" in options:
                        animal.alimentacion.eliminar_alimentos_disponibles()
                    st.success("El producto fue actualizado correctamente")



    def obtener_Dato_String(self, mensaje):
        return st.text_input(mensaje)

    def obtener_Dato_Int(self, mensaje):
        return st.number_input(mensaje)

    def obtener_Dato_Int_Rango(self, mensaje, min_value=0, max_value=0):
        return st.number_input(mensaje, min_value=min_value, max_value=max_value)

    def escoger_Alimentacion(self):

        dietasDisponible = ["carnivora", "herbivora", "omnivora"]

        option = st.selectbox(
            'Tipo de dieta',
            dietasDisponible)

        st.write('Has seleccionado la dieta:', option)

        return option

    def pedir_salud(self):
        salud = input("Ingrese el estado actual de salud del animal: ")
        return salud

    def mostrar_mensaje_exitoso(self, mensaje):
        st.success(mensaje)

    def mostrar_mensaje_error(self, mensaje):
        st.error(mensaje)

    def listar_atributos_animal(self, animal):
        st.divider()
        with st.container():
            st.subheader("Esta es la información actual de animal")
            datos = pd.DataFrame(
                self.controlador.aplicar_formato_tabla(animal),
                columns=["ID", "Nombre", "Especie", "Estado de salud", "horas de sueño", "Número de juguetes"]
            )
            st.table(datos)

    def listar_alimentos_animal(self, animal):
        st.divider()
        with st.container():
            st.subheader("Esta es la información actual de animal")
            print(animal.alimentacion.alimentosAnimal)
            datos = pd.DataFrame(
                self.controlador.aplicar_formato_alimentos(animal.alimentacion.alimentosAnimal),
                columns=["Cantidad de kg", "Nombre"]
            )
            st.table(datos)

    def agregar_alimentos(self, animal, lista_alimentos, num):

        kgs = []
        col1, col2 = st.columns([3, 1])
        i = 0
        while i < len(lista_alimentos):
            with st.container():
                kg = st.slider(f"Kilogramos de {lista_alimentos[i]}:", 0, 50, 25, key=i+num)
                print(i)
                kgs.append(kg)
            i += 1

        for clave in range(len(lista_alimentos)):
            animal.alimentacion.alimentosAnimal[lista_alimentos[clave]] = kgs[clave]



    def agregar_juguetes(self, animal, cantJuguetes, num):

            col1, col2 = st.columns([3, 1])
            i = 1
            while i <= cantJuguetes:
                with st.container():
                    nombre = col1.text_input(f"Nombre juguete {i}:", key=num+i)
                    animal.juguetes.append(nombre)
                    print(f"key:{i}")
                i += 1
