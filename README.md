# Zoo-Python-MAVA

## Table de contenido

1. [Introducción](#Introducción)
2. [Links](##Links)
3. [Models](##Models)
4. [View](##View)
5. [Controller](##Controller)
6. [Diagramadeclases ](##Diagramadeclases)


## Introducción

Este proyecto consiste en la implementación de un programa en Python que simula el funcionamiento de un zoológico. El programa se encuentra alojado en la nube como una aplicación, lo que permite una interacción más amigable entre el usuario y el programa.
El programa está organizado en tres directorios principales: models, view y controller. Estos directorios interactúan entre sí durante toda la ejecución del programa, facilitando su funcionamiento.
En el directorio **'models'** se encuentran los modelos de datos utilizados en el programa, que representan los elementos del zoológico, como los animales, hábitats, entre otros.
El directorio **'view'** contiene los archivos relacionados con la interfaz de usuario, incluyendo las pantallas, formularios y elementos visuales necesarios para una experiencia interactiva.
El directorio **'controller'** alberga los controladores, que son responsables de gestionar la lógica del programa, coordinando la interacción entre los modelos de datos y la interfaz de usuario.
Esta estructura de directorios permite una organización clara y modular del programa, facilitando su mantenimiento y escalabilidad. A través de la interacción entre estos directorios, se logra una simulación fluida y eficiente del funcionamiento de un zoológico en este proyecto.

## Links
***Link de la app en la nube***
> [Zoologico MAVA](https://mariap4444-zoo-python-mava-main-st4qly.streamlit.app/).

***Pruebas fotogradicas del funcionamiento del programa***
>[Fotos](https://docs.google.com/document/d/1as9BL2eZd2aE90gHLmLe5TFWuYKQQODsJ4FaMV3jbNA/edit?usp=sharing)

***Informe de autoevaluacion - Maria Paula Castillo Erazo***
>[Informe de autoevaluacion](https://docs.google.com/document/d/1-9KDn4kOjMJntsmQ_INNvbP1aY5lAVOe5y_8ggyraiE/edit?usp=sharing)

***Informe de autoevaluacion - Maria Paula Castillo Erazo***
>[Informe de autoevaluacion](https://docs.google.com/document/d/1FJ8sV5x6Aa_KVZXBgxTE25b18naBJFcWhNuO-0G1TPE/edit?usp=sharing)

## Models
En este directorio se encuentran nuestras 4 principales clases:
1. ### Alimentacion
   Esta clase se encarga de gestionar la alimentación de nuestros animales. Contiene los siguientes parámetros:
    - **tipoDieta:** Representa el tipo de dieta del animal (carnívora, herbívora, omnívora).
    -  **alimentosDisponibles:** Una lista que contiene los alimentos disponibles para el animal.
    * **alimentosAnimal:** Un diccionario que registra los alimentos de la dieta actual del animal, utilizando como llave el nombre del alimento y como valor la cantidad en Kg
  
     Estos parámetros son fundamentales para el control y seguimiento de la alimentación de los animales en nuestro sistema. Esta clase se encarga de administrar y manejar estos aspectos relacionados con la alimentación de los animales. Esta clase cuenta a su vez con métodos como:
    * def eliminarAlimentoAnimal(self, alimentoEliminar): Esta función también permite eliminar un alimento específico de la dieta actual de un animal. Esto resulta útil en situaciones en las que, durante la vida del animal, sea necesario dejar de ingerir cierto alimento. Con esta función, el usuario puede seleccionar y eliminar de manera sencilla el alimento deseado de la dieta del animal, garantizando así una gestión flexible y adaptable de su alimentación a lo largo del tiempo.
    
    * def designadorDeAlimentosDispo(self): Esta función ha sido diseñada con el objetivo de asignar automáticamente los posibles alimentos que un animal puede ingerir inicialmente, una vez que el usuario ingrese su tipo de alimentación (carnívora, herbívora u omnívora). Esto se logra a través del atributo 'alimentosDisponibles'. Además, este atributo puede ser modificado en cualquier momento durante la ejecución del programa, lo que permite ajustar la dieta del animal según sea necesario.
    
    * def listaAlimentosDisponibles(self): Esta función ha sido diseñada con el objetivo de permitir a los usuarios cambiar su dieta actual de animales. Al utilizar esta función, los usuarios pueden visualizar los alimentos disponibles y seleccionar aquellos que deseen agregar a su dieta actual. De esta manera, se facilita la elección y personalización de la alimentación de los animales.
    
    * def listarAlimentosAnimal(self, mensaje): Esta función ha sido diseñada con el propósito de listar los alimentos que componen la dieta actual del animal. Su objetivo principal es permitir al usuario visualizar los alimentos presentes en la dieta y facilitar la selección de aquellos que desee eliminar. Al ejecutar esta función, se mostrará una lista de los alimentos que forman parte de la dieta actual del animal. Esto proporcionará al usuario una visión general de los alimentos presentes y permitirá una toma de decisiones informada para eliminar aquellos que se consideren necesarios.
    
    * def imprimirListaAlimentosAnimal(self): Esta función ha sido diseñada para mostrar la información de la dieta actual en la aplicación cada vez que se llama. Su objetivo principal es permitir al usuario visualizar de manera clara y organizada los alimentos presentes en la dieta actual, incluyendo el nombre de los alimentos y sus respectivos valores en kg. De esta manera, el usuario puede tener un seguimiento preciso de la alimentación del animal.



2. ### Animal
    Esta clase se encarga de gestionar toda la información relacionada con nuestro animal. Incluye los siguientes atributos:
    -  nombre: El nombre del animal.
    -  especie: La especie a la que pertenece el animal.
    -  estadoDeSalud: El estado de salud del animal.
    -  alimentacion: Un objeto que gestiona la alimentación del animal.
    -  id: El identificador único del animal.
    -  edad: La edad del animal.
    -  tempMaxA: La temperatura máxima soportada por el animal.
    -  tempMinA: La temperatura mínima soportada por el animal.
    -  cantHorasDormidas: La cantidad de horas que el animal duerme.
    -  juguetes: Una lista que contiene los juguetes del animal.
    -  cantMaxDormir: La cantidad máxima de horas que el animal puede dormir.
    -  jugar = booleano que nos permite conocer si el animal ya jugo 
    -  comer =  booleano que nos permite conocer si el animal ya comió  
    
    Esta clase cuenta a su vez con el siguiente método:
    - def imprimirJuguetes(self):Esta función ha sido desarrollada con el propósito de mostrar al usuario los juguetes que el animal posee una vez que se llama. Su objetivo principal es permitir al usuario visualizar de manera clara y organizada los juguetes disponibles para el animal en cuestión.
3. ### Hábitat
    Esta es una clase padre la cual tendrá 4 clases hijas, estas definen los tipos de hábitats (selvático, desértico, polar, acuático), la clase padre cuenta con los siguientes atributos:
    - Nombre: Representa el nombre del hábitat.
    - Temperatura Máxima: Indica la temperatura máxima registrada en el hábitat.
    - Temperatura Mínima: Indica la temperatura mínima registrada en el hábitat.
    - Animales: Es un diccionario que almacena los animales presentes en el hábitat, donde las claves son los id de los animales y los valores son objetos que representan a cada animal.
    - Dieta: Define la dieta predominante en el hábitat, es decir, el tipo de alimentación de los animales presentes.
    - Cantidad Máxima de Animales: Representa la cantidad máxima de animales que puede albergar el hábitat.
    
    La clase Habitat también tiene un método llamado agregarAnimal que permite agregar un nuevo animal al hábitat.
Las clases derivadas, HabitatSelvatico, HabitatAcuatico, HabitatPolar y HabitatDesertico heredan de la clase base Habitat y añaden atributos específicos para cada tipo de hábitat.
La clase HabitatAcuatico tiene los siguientes atributos adicionales:
    - salinidad: la salinidad del agua en el hábitat acuático.
    - profundidad: la profundidad del agua en el hábitat acuático.
    
    La clase HabitatPolar tiene los siguientes atributos adicionales:
    - cantidadHielo: la cantidad de hielo presente en el hábitat polar.
    - tamanioCueva: el tamaño de la cueva en el hábit	
    
    La clase HabitatDesertico hereda de la clase base Habitat y añade dos atributos adicionales:
    - humedad: la humedad en el hábitat desértico.
    - cantidadOasis: la cantidad de oasis en el hábitat desértico.
    
    La clase HabitatSelvatico también hereda de la clase base Habitat y tiene dos atributos específicos:
    - cantidadArboles: la cantidad de árboles en el hábitat selvático.
    - cantidadRios: la cantidad de ríos en el hábitat selvático.
4. ### Zoo
    Esta es la clase contenedora, en la cual se basa todo el sistema, dentro de ella guardamos y añadimos hábitats. Cuenta con los siguientes atributos:
    - registroAn = para almacenar los animales sin hábitat
    - cantAnimales =  sirve para asignarle los ids a los animales 
    - habitats = lista para almacenar los hábitats del zoológico.
    
    Esta clase cuenta a su vez con métodos como:
     - eliminarAnimalRegistro(self, id): Este método se utiliza para eliminar un animal del registro utilizando su ID como clave en el diccionario registroAn una vez este animal este relacionado con un hábitat.
     - agregarAnimalRegistro(self, animalNuevo): Este método se utiliza para agregar un nuevo animal al registro. El animal se agrega como un valor en el diccionario registroAn, utilizando su ID como clave.
     - agregarHabitat(self, habitat): Este método se utiliza para agregar un nuevo hábitat a la lista habitats del zoológico.
     - listarAnimalesRegistro(self): Este método muestra una lista de los animales en el registro (sin hábitat) y permite al usuario seleccionar uno de ellos. Devuelve el animal seleccionado para poder agregarlo al hábitat que se desee.
     - listarHabitatasDiponiblesAnimal(self, animal): Este método muestra una lista de los hábitats disponibles para un animal dado. Los hábitats disponibles cumplen con ciertas condiciones, como tener suficiente capacidad, temperatura adecuada y dieta compatible. El usuario puede seleccionar uno de los hábitats disponibles y el método devuelve el hábitat seleccionado.
     - buscarAnimalIdYAgregar(self, id, animalModificado): Este método busca un animal en todos los hábitats y en el registro utilizando su ID. Si encuentra el animal, lo reemplaza por el animal modificado.
     - listarAnimalesEnHabitat(self): Este método lista todos los animales en los hábitats y en el registro y permite al usuario seleccionar uno de ellos. Devuelve el animal seleccionado, para que pueda modificar la información o interactuar con él.
     - listarInfoCompletaZoo(self): Este método muestra información completa sobre el zoológico, incluyendo los animales en el registro y en los hábitats. Utiliza la biblioteca Streamlit para crear una interfaz interactiva con expanders y subheaders.

## View
En este directorio se encuentra la clase zooView la cual utiliza la biblioteca streamlit para crear una interfaz gráfica y mostrar elementos como botones, campos de entrada y listas desplegables para que el usuario pueda realizar acciones y proporcionar información.
Cuando se inicializa la clase se realiza dos tareas importantes:
- Crea una instancia del modelo Zoo, que es una representación del zoológico y sus componentes
- Crea una instancia del controlador zooController, que es responsable de manejar las acciones y la lógica detrás de las interacciones del usuario.

Después esta clase cuenta con los siguientes métodos:
- def prueba(self): Este método muestra el menú principal de la interfaz de usuario. Utiliza la biblioteca streamlit para crear botones y mostrar un título. Los botones representan diferentes opciones que el usuario puede seleccionar, como agregar hábitat, agregar animal, listar animales, etc. Dependiendo del botón seleccionado, se envía la opción correspondiente al controlador para manejarla adecuadamente.
- def seleccionar_Habitat(self): Este método muestra opciones para seleccionar el tipo de hábitat que se va a crear en el zoológico. Utiliza la función st.radio de la biblioteca streamlit para mostrar botones de opción y permite al usuario seleccionar uno. Luego, dependiendo de la opción seleccionada (selvático, desértico, acuático o polar), se muestra información relacionada con ese tipo de hábitat. Por último, la opción seleccionada se devuelve para ser utilizada en la creación del hábitat.
- def escoger_actividad(self): Este método muestra opciones para seleccionar una actividad que se puede realizar con un animal en el zoológico. Utiliza la función st.selectbox de streamlit para mostrar una lista desplegable con las opciones disponibles (comer, dormir, jugar). El usuario puede seleccionar una opción y luego se devuelve la opción seleccionada.
- def interactuar_animal(self): Este método permite al usuario interactuar con un animal en el zoológico. Primero, muestra una lista de animales disponibles utilizando el método listarAnimalesEnHabitat() del modelo Zoo. Luego, utiliza el método escoger_actividad() para que el usuario seleccione una actividad (comer, dormir, jugar). Dependiendo de la actividad seleccionada, se realizan diferentes acciones, como seleccionar un alimento para el animal, especificar la cantidad de horas de sueño o seleccionar un juguete. Se muestra un mensaje exitoso o de error según el resultado de la interacción.
- def menu_info_animal(self, animal): Este método muestra algunos atributos del animal seleccionado y permite al usuario seleccionar los atributos que desea editar. Utiliza el método listar_atributos_animal(animal) para mostrar los atributos del animal y luego muestra una lista de opciones para editar esos atributos. El usuario puede seleccionar múltiples opciones y se devuelve una lista con las opciones seleccionadas.
- def obtener_Dato_String(self, mensaje), obtener_Dato_Int(self, mensaje), obtener_Dato_Int_Rango(self, mensaje, min_value, max_value): Estos métodos que solicitan datos al usuario en forma de cadenas de texto o números enteros. Muestran un mensaje al usuario y utilizan la función st.text_input o st.number_input de streamlit para obtener la entrada del usuario. Dependiendo del tipo de dato solicitado, se valida que el valor ingresado sea válido y se devuelve el dato obtenido.
- Método escoger_Alimentacion(self): Este método muestra opciones para seleccionar el tipo de alimentación que se desea agregar a un animal o a un hábitat. Utiliza la función st.radio de streamlit para mostrar botones de opción con las diferentes opciones de alimentación. El usuario puede seleccionar una opción y se devuelve la opción seleccionada.
- def mostrar_mensaje_exitoso(self, mensaje): Este método muestra un mensaje que confirma que una acción se ha llevado a cabo correctamente. Utiliza la función st.success(mensaje) de streamlit para mostrar el mensaje con un estilo visual de éxito.
- def mostrar_mensaje_error(self, mensaje): Este método muestra un mensaje que indica que no se ha podido llevar a cabo una acción correctamente. Utiliza la función st.error(mensaje) de streamlit para mostrar el mensaje con un estilo visual de error.
- def listar_atributos_animal(self, animal): Este método se utiliza en la opción de editar animal. Muestra una tabla que contiene los atributos básicos del animal, como su ID, nombre, especie, estado de salud, horas de sueño y número de juguetes. Utiliza la función st.table(datos) de streamlit para mostrar la tabla con los datos del animal.
- def listar_alimentos_animal(self, animal): Este método se utiliza en la opción de editar animal. Muestra una tabla que muestra cada alimento del animal y la cantidad de kilogramos correspondiente. Utiliza la función st.table(datos) de streamlit para mostrar la tabla con los datos de los alimentos del animal.
- def agregar_juguetes(self, animal, cantJuguetes, num): Este método se utiliza en la opción de editar animal. Permite agregar juguetes a la lista de juguetes de un animal. Recibe como parámetros el objeto animal, la cantidad de juguetes a agregar (cantJuguetes) y un número de identificación (num). Utiliza la función st.text_input para obtener el nombre de cada juguete nuevo y lo agrega a la lista de juguetes del animal si no está presente.
- def informacionAPI(self) realiza una consulta a una API de perros para obtener información y mostrar una imagen de una raza específica.


## Controller
En este directorio nos encontramos con un controlador de un zoológico implementado en Python utilizando el framework Streamlit. El controlador se encarga de manejar las diferentes acciones y operaciones relacionadas con el zoológico, como la creación de hábitats, la creación de animales, la edición de animales, la vinculación de animales y hábitats, etc.

El controlador tiene un método principal llamado menu_principalV2 que recibe una opción y realiza diferentes acciones dependiendo de la opción seleccionada. A continuación, se explican las principales funciones y métodos presentes en la clase:
- def editarAniml(self): El método editarAniml se encarga de editar los atributos de un animal. Permite cambiar el nombre, la edad, el estado de salud, las horas de sueño, la cantidad de kg en la dieta, agregar o eliminar juguetes, agregar o eliminar alimentos en la dieta, etc.
- def vincular_Animal_Habitat(self): El método vincular_Animal_Habitat permite vincular un animal a un hábitat. Muestra una lista de animales disponibles y una lista de hábitats disponibles, y permite agregar un animal a un hábitat seleccionado.
- def crear_Habitat(self): El método crear_Habitat se encarga de crear un nuevo hábitat. Solicita al usuario información sobre el tipo de hábitat, el tipo de alimentación, la capacidad máxima de animales, y otros atributos específicos según el tipo de hábitat seleccionado.
- def crear_animal se encarga de recopilar los datos necesarios para crear un nuevo animal. Primero, muestra un formulario en la interfaz gráfica donde el usuario puede ingresar información como el nombre, especie, estado de salud, edad, temperatura máxima, horas de sueño y juguetes del animal. Luego, permite seleccionar los alimentos disponibles para el animal y establecer la cantidad en kilogramos de cada alimento seleccionado. Finalmente, verifica que se hayan proporcionado todos los datos necesarios y muestra un botón para crear el nuevo animal. Si se hace clic en el botón, la función devuelve el objeto nuevoAnimal que contiene todos los datos ingresados.
- Las funciones aplicar_formato_tabla y aplicar_formato_alimentos se utilizan para formatear los datos del animal y los alimentos en forma de tablas para su visualización en la interfaz gráfica.

## Diagramadeclases

![Diagrama de clases](https://github.com/MariaP4444/Zoo-Python-MAVA/blob/1c93a73bb263bcc0c68abb6965f382afe3b73f2e/crud.drawio.png)
