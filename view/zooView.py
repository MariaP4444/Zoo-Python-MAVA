import models.Zoo as zooModel
import streamlit as st
import controller.zooContrller as zooController


class zooView:
    def __init__(self):
        self.zoo = zooModel.Zoo()
        self.controlador = zooController.zooController(self.zoo, self)


    def prueba(self):
        opcion = 0

        st.title("Bienvenido el zoologico MAVA")

        with st.container():
            col1, col2, col3, col4, col5 = st.columns(5)
            boton_agregar_habitat = col1.button("Agregar habitat", 1)
            boton_agregar_animal = col2.button("Agregar animal", 2)
            boton_listar_habitats = col3.button("Listar animales", 3)
            boton_modificar_infoAn = col4.button("Editar animal", 4)
            boton_visitar_habitat = col5.button("Interactuar con animal", 5)

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

        if "opcion" in st.session_state:
            self.controlador.menu_principalV2(st.session_state["opcion"])



    def crear_animal_prueba(self, zoo):
        listaDatos = []
        st.divider()
        with st.container():
            st.subheader("Formulario para crear un nuevo producto")
            nombre = st.text_input("Nombre:")
            listaDatos.append(nombre)

            especie = st.text_input("Especie:")
            listaDatos.append(especie)

            salud = st.text_input("Estado de salud:")
            listaDatos.append(salud)

            listaDatos.append(zoo.cantAnimales)
            self.zoo.cantAnimales+=1

            edad = st.number_input("Edad:", min_value=0, max_value=100)
            listaDatos.append(edad)

            tempMax = st.number_input("Temperatura máxima")
            listaDatos.append(tempMax)

            tempMin = st.number_input("Temperatura mínima", max_value=tempMax)
            listaDatos.append(tempMin)

            hSuenio = st.number_input("Horas de sueño:", min_value=0, max_value=24)
            listaDatos.append(hSuenio)

            cantJuguetes = st.number_input("Cantidad de juguetes:", min_value=1, max_value=15)
            lista_juguetes = []
            if cantJuguetes:
                col1, col2 = st.columns([3,1])
                i=1
                while i <= cantJuguetes:
                    with st.container():
                        nombre = col1.text_input(f"Nombre juguete {i}:", key=i+95)
                        print(i)
                        lista_juguetes.append(nombre)
                    i+=1
            listaDatos.append(lista_juguetes)

            option = st.selectbox(
                'Tipo de dieta',
                ('Carnivora', 'Herbivora', 'Omnivora'))

            st.write('Has seleccionado la dieta:', option)

            listaDatos.append(option)

            boton_accion = st.button("Crear nuevo producto")

            if boton_accion:
                return listaDatos


    def preguntar_id(self):
        id = st.number_input("Ingrese el id del animal: ", min_value=0)
        return id

    def menu_info_animal_prueba(self, animal):
        print(print(animal.nombre))
        option = st.selectbox(
            'How would you like to be contacted?',
            ('Edad', 'Estado de salud', 'Horas de sueño', 'Cantidad de kg en dieta', 'Agregar juguetes', 'Eliminar juguetes', 'Agregar alimento', 'Eliminar alimento'))

        st.write('You selected:', option)



    def menu_info_animal_V(self, animal):
        terminado = False
        while not terminado:
            print("\n** Seleccione el dato a cambiar **")
            print("1. Edad")
            print("2. Estado de salud")
            print("3. Horas de sueño máximas")
            print("4. Cantidad de kg en dieta")
            print("5. Agregar juguetes")
            print("6. Eliminar juguete")
            print("7. Agregar alimento a la dieta del animal")
            print("8. Eliminar alimento de la dieta del animal")
            print("0. Guardar y salir")

            opcion = int(input())

            self.controlador.menu_cambiar_infoAn(opcion, animal)

            if opcion == 0:
                print("Adios!")
                terminado = True
            if opcion < 0 or opcion > 8:
                print("Opción inválida. Inténtalo de nuevo.")

            print(animal.edad)

    def obtener_Dato_String(self, mensaje):
        return st.text_input(mensaje)

    def obtener_Dato_Int(self, mensaje):
        return st.number_input(mensaje)

    def obtener_Dato_Int_Rango(self, mensaje, min_value=0, max_value=0):
        return st.number_input(mensaje, min_value=min_value, max_value=max_value)

    def escoger_Dieta(self):

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