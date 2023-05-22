import models.Zoo as zooModel
import streamlit as st
import controller.zooContrller as zooController
import pandas as pd


class zooView:
    def __init__(self):
        self.zoo = zooModel.Zoo()
        self.controlador = zooController.zooController(self.zoo, self)


    """ PRUEBA
     Presenta el menu principal mediante botones, los cuales son:
     - Agregar hábitat
     - Agregar animal
     - Listar animales
     - Editar animal
     - Interactuar con animal
     - Vincular animal con un habitat
     Segun el boton escogido, envia una opcion al controlador
    """
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

        #st.write(self.zoo.habitats[0].animales[2].nombre)
        if "opcion" in st.session_state:
            self.controlador.menu_principalV2(st.session_state["opcion"])


    """ SELECCIONAR HABITAT
        Opcion: Agregar habitat
        Prsesenta los tipos de habitat mediante opciones (Selvatico, desertico acuatico, polar)
        Retorna la opcion escogida a la funcion de crear habitat
    """
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


    """ ESCOGER ACTIVIDAD
     Opcion: Interactuar con animal
     Muestra como opciones las 3 actividades que se pueden hacer con un animal.
     Una vez escogida, se retorna a la funcion interactuar_animal para realizar la accion deseada
    """
    def escoger_actividad(self):

        actividades = ['comer', 'dormir', 'jugar']

        option = st.selectbox(
            'Tipo de dieta',
            actividades)
        return option


    """ ESCOGER ACTIVIDAD
     Opcion: Interactuar con animal
     Presenta las 3 opciones para interactuar con el animal: (comer, dormir, jugar)
     Segun la opcion, revisa si el animal ya ha dormido la cantidad maxima de horas, si ya ha comido, y si ya ha jugado.
     Si no lo ha hecho, le permite al usuario
     Comer: escoger un alimento de la dieta actual
     Dormir: decidir la cantidad de horas(min= 1, max= cantHorasDormidas)
     Jugar: escoger un juguete del animal
    """
    def interactuar_animal(self):

        animal = self.zoo.listarAnimalesEnHabitat()

        option = self.escoger_actividad()

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


    """ MENU INFO ANIMAL
     Opcion: editar animal
     Muestra algunos atributos del animal
     Presenta las opciones para editar animal, que son los atributos que se pueden cambiar de cada animal
     Retorna la opcion escogida a la funcion editar animal   
    """
    def menu_info_animal(self, animal):

        self.listar_atributos_animal(animal)
        datos_cambiar = ['Nombre', 'Edad', 'Estado de salud', 'Horas de sueño', 'Cantidad de kg en dieta', 'Agregar juguetes', 'Eliminar juguetes', 'Agregar alimento a dieta actual', 'Eliminar alimento en dieta actual', 'Agregar alimento a dieta disponible']


        options = st.multiselect(
            'Elige los datos a editar',
            datos_cambiar)

        return options


    """ OBTENER DATO STRING
     Pide un dato al usuario en forma de string, con un mensaje que le indica lo que debe ingresar.
     Retorna la cadena a varias funciones que requieren un input del tipo string
    """
    def obtener_Dato_String(self, mensaje):
        return st.text_input(mensaje)


    """ OBTENER DATO INT
     Pide un dato al usuario en forma de entero, con un mensaje que le indica lo que debe ingresar.
     Retorna la cadena a varias funciones que requieren un input del tipo entero
    """
    def obtener_Dato_Int(self, mensaje):
        return st.number_input(mensaje)


    """ OBTENER DATO INT RANGO
     Pide un dato al usuario en forma de entero, con un mensaje que le indica lo que debe ingresar, y el rango en el que debe estar el numero
     Retorna la cadena a varias funciones que requieren un input del tipo entero dentro de un rango
    """
    def obtener_Dato_Int_Rango(self, mensaje, min_value=0, max_value=0):
        return st.number_input(mensaje, min_value=min_value, max_value=max_value)


    """ ESCOGER ALIMENTACION
     Presenta los 3 tipos de alimentacion, devuelve la opcion escogida a la funcion crear animal y crear habitat
    """
    def escoger_Alimentacion(self):

        dietasDisponible = ["carnivora", "herbivora", "omnivora"]

        option = st.selectbox(
            'Tipo de dieta',
            dietasDisponible)

        st.write('Has seleccionado la dieta:', option)

        return option


    """ MENSAJE EXITOSO
     Muestra un mensaje que confirma que una accion se ha llevado a cabo correctamente
    """
    def mostrar_mensaje_exitoso(self, mensaje):
        st.success(mensaje)


    """ MENSAJE ERROR
     Muestra un mensaje que indica que no se ha podido llevar a cabo una accion correctamente
    """
    def mostrar_mensaje_error(self, mensaje):
        st.error(mensaje)


    """ LISTAR ATRIBUTOS ANIMAL
     Opcion: editar animal
     Presenta una tabla que muestra atributos basicos del animal
    """
    def listar_atributos_animal(self, animal):
        st.divider()
        with st.container():
            st.subheader("Esta es la información actual de animal")
            datos = pd.DataFrame(
                self.controlador.aplicar_formato_tabla(animal),
                columns=["ID", "Nombre", "Especie", "Estado de salud", "horas de sueño", "Número de juguetes"]
            )
            st.table(datos)


    """ LISTAR ALIMENTOS ANIMAL
     Opcion: Editar animal
     Presenta una tabla que muestra cada alimento del animal y la cantidad de kg correspondiente
    """
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


    """ AREGAR JUGUETES
     Opcion: Editar animal
     Dada una lista de juguetes nuevos, los agrega a la lista de juguetes de un animal
    """
    def agregar_juguetes(self, animal, cantJuguetes, num):

            col1, col2 = st.columns([3, 1])
            i = 1
            while i <= cantJuguetes:
                with st.container():
                    nombre = col1.text_input(f"Nombre juguete {i}:", key=num+i)
                    if nombre:
                        if nombre not in animal.juguetes:
                            animal.juguetes.append(nombre)
                    print(f"key:{i}")
                i += 1
