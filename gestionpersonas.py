from persona import Persona

class GestorPersonas:
    def __init__(self):
        self.personas = []

    def agregar_persona(self, nombre, apellido, edad, documento, gmail, lugar_vive):
        persona = Persona(nombre, apellido, edad, documento, gmail, lugar_vive)
        self.personas.append(persona)
        print("Persona agregada exitosamente.\n")

    def mostrar_personas(self):
        if not self.personas:
            print("No hay personas registradas.\n")
        else:
            print("lista de Personas:")
            for p in self.personas:
                print(p)
            print()
