
from typing import List, Dict
import streamlit as st
class Animal:
    def _init_(self, nombre="", especie="", estadoDeSalud="", id=0, tempMaxA=0, tempMinA=0, cantMaxDormir=0, edad=0,
               juguetes=[],
               alimentacion=None, jugar=False, comer=False, cantHorasDormidas=0):

        self.nombre = nombre
        self.especie = especie
        self.estadoDeSalud = estadoDeSalud
        self.alimentacion = alimentacion
        self.id = id
        self.edad = edad
        self.tempMaxA = tempMaxA
        self.tempMinA = tempMinA
        self.cantHorasDormidas = cantHorasDormidas
        self.juguetes = juguetes
        self.cantMaxDormir = cantMaxDormir
        self.jugar = jugar
        self.comer = comer

    """ IMPRIMIR JUGUETES
     Opcion: Listar animales
     Muestra cada juguete de la lsita de juguetes de un animal
    """
    def imprimirJuguetes(self):
        for juguete in self.juguetes:
            st.write("     -- Nombre: ", juguete)

