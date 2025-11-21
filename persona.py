
# persona.py
# En este archivo se define la clase Persona.Una Persona guarda información básica como nombre, apellido,edad, documento de identidad, correo y lugar donde vive.

class Persona  :
    def __init__(self, nombre, apellido, edad, documento, gmail, lugar_vive):
        """
        Constructor de la clase Persona.
        Aquí se inicializan todos los atributos que forman
        parte de una persona.
        
        :param nombre: Nombre de la persona
        :param apellido: Apellido de la persona
        :param edad: Edad en años
        :param documento: Documento de identidad (C.C o T.I)
        :param gmail: Correo electrónico
        :param lugar_vive: Ciudad o lugar donde vive
        """
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento = documento
        self.gmail = gmail
        self.lugar_vive = lugar_vive

    def __str__(self):# También incluye un método para mostrar sus datos en texto.
        """
        Representación en texto de la persona.
        Este método permite imprimir una persona de forma legible.
        """
        return (f"Nombre: {self.nombre} {self.apellido} | "
                f"Edad: {self.edad} | "
                f"C.C o T.I: {self.documento} | "
                f"Gmail: {self.gmail} | "
                f"Lugar donde vive: {self.lugar_vive}")
