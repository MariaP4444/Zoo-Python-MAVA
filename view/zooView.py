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

