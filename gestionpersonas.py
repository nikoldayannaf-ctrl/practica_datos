# gestionar_personas.py
from persona import Persona  # Importamos la clase Persona para poder crear instancias

class GestorPersonas:# Este archivo contiene la clase GestorPersonas, que se encarga de administrar una lista de personas.
    def __init__(self):
        """
        Constructor de GestorPersonas.
        Inicializa una lista vacía que almacenará todas las personas.
        """
        self.personas = []

    def agregar_persona(self, nombre, apellido, edad, documento, gmail, lugar_vive):# Permite agregar nuevas personas y mostrarlas.
        """
        Crea una nueva Persona y la agrega a la lista de personas.
        
        :param nombre: Nombre de la persona
        :param apellido: Apellido de la persona
        :param edad: Edad en años
        :param documento: Documento de identidad
        :param gmail: Correo electrónico
        :param lugar_vive: Ciudad o lugar donde vive
        """
        persona = Persona(nombre, apellido, edad, documento, gmail, lugar_vive)
        self.personas.append(persona)
        print("Persona agregada exitosamente.")  # Confirmación al usuario

    def mostrar_personas(self):
        """
        Muestra todas las personas registradas en la lista.
        Si no hay personas, muestra un mensaje indicando que la lista está vacía.
        """
        if not self.personas:
            print("No hay personas registradas.")
        else:
            print("Lista de Personas:")
            for p in self.personas:
                print(p)  # Llama al método __str__ de la clase Persona
            print()
