import models.Zoo as zooModel
import models.habitat as habitatModel
import controller.zooContrller as zooController

class zooView:
    def menu_principalV(self):
        opcion = -1
        zoo = zooModel.Zoo()

        while opcion != 0:
            print("\n~~~~~~~~~~~~~~~~~~~~~ ZOO:", zoo.nombre , "~~~~~~~~~~~~~~~~~~~~~\n")
            print("1. Agregar habitat")
            print("2. Agregar animal")
            print("3. Lista de habitats y animales")
            print("4. Modificar informacion de animal")
            print("5. Visitar habitat")
            print("0. Salir")
            opcion = int(input("Escoge una opcion: "))

            controlador = zooController.zooController(zoo, self)
            controlador.menu_principal(opcion)

            if opcion == 0:
                print("Adios!")
            if opcion < 0 or opcion > 5:
                print("Opción inválida. Inténtalo de nuevo.")


    def crear_animal(self, zoo):
        listaDatos = []
        juguetes_temp = []

        ##ingresa nombre [0]
        listaDatos.append(input("Ingrese el nombre del animal:"))

        ##Ingresa especie [1]
        listaDatos.append(input("Ingrese la especie del animal:"))

        ##Ingresa estado de salud [2]
        listaDatos.append(input("Ingrese el estado de salud del animal:"))

        ##Ingresa id [3]
        listaDatos.append(zoo.cantAnimales)
        zoo.cantAnimales += 1

        while True:
            try:
                print("Ingrese la edad del animal:")
                edad = int(input())
                if edad <= 0 or edad > 100:
                    raise ValueError("La edad debe ser un entero positivo menor o igual a 100")
                break
            except ValueError:
                 print("Se ingresó un argumento inválido. Por favor ingrese un número entero.")

        ##Ingresa edad [4]
        listaDatos.append(input(edad))

        tempMaxA = int(input("Ingrese la temperatura maxima: "))
        ##Ingresa temperatura maxima [5]
        listaDatos.append(input(tempMaxA))

        while True:
            try:
                print("Ingrese la temperatura minima del animal: ")
                tempMinA = int(input())
                if tempMinA > tempMaxA:
                    raise ValueError("La temperatura maxima es menor que la temperatura minima")
                break
            except ValueError:
                print("Se ingresó un argumento inválido. Por favor ingrese un numero menor a la temperatura maxima.")

        ##Ingresa temperatura minima [6]
        listaDatos.append(tempMinA)

        while True:
            try:
                print("Ingrese las horas de sueño del animal:")
                cant_max_dormir = int(input())
                if cant_max_dormir <= 0:
                    raise ValueError("La cantidad de horas de sueño debe ser un entero positivo")
                break
            except ValueError:
                print("Se ingresó un argumento inválido. Por favor ingrese un número entero.")

        ##Ingresa horas de suenio [7]
        listaDatos.append(cant_max_dormir)

        while True:
            try:
                print("Ingrese el número de juguetes que va a tener el animal:")
                cant_juguetes = int(input())
                if cant_juguetes <= 0:
                    raise ValueError("La cantidad de juguetes debe ser un entero positivo")
                break
            except ValueError:
                print("Se ingresó un argumento inválido. Por favor ingrese un número entero.")

        for i in range(cant_juguetes):
            print(f"Ingrese el nombre del juguete {i + 1}:")
            juguete_nom = input().lower()
            juguetes_temp.append(juguete_nom)

        listaDatos.append(juguetes_temp)

        while True:
            print("\nTipo de dieta disponible:")
            print("\n - Carnivoro \n - Herbivoro \n - Omnivoro")
            print("Ingrese el tipo de alimentación del animal:")
            alimentacion = input().lower()
            if zoo.lista_dietas_disponibles(alimentacion):
                break
            else:
                print("La dieta ingresada no está disponible. Por favor ingrese una dieta válida.")

        listaDatos.append(alimentacion)

        return listaDatos

    def preguntar_id(self):
        id = int(input("Ingrese el id del animal: "))
        return

    #def mostrar_mensaje_exitoso(self, mensaje):
    #    st.success(mensaje)

    #def mostrar_mensaje_error(self, mensaje):
    #    st.error(mensaje)