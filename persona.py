class Persona:
    def __init__(self, nombre, apellido, edad, documento, gmail, lugar_vive):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento = documento
        self.gmail = gmail
        self.lugar_vive = lugar_vive

    def __str__(self):
        return (f"Nombre: {self.nombre} {self.apellido} | "
                f"Edad: {self.edad} | "
                f"C.C o T.I: {self.documento} | "
                f"Gmail: {self.gmail} | "
                f"Lugar donde vive: {self.lugar_vive}")
