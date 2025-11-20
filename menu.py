from gestionpersonas import GestorPersonas

def main():
    gestor = GestorPersonas()

    while True:
        print("--- Menú ---")
        print("1. Agregar persona")
        print("2. Mostrar personas")
        print("3. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = input("Edad: ")
            documento = input("Documento: ")
            gmail = input("Gmail: ")
            lugar_vive = input("Lugar donde vive: ")

            gestor.agregar_persona(nombre, apellido, edad, documento, gmail, lugar_vive)

        elif opcion == "2":
            gestor.mostrar_personas()

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intente nuevamente.\n")

if __name__ == "__main__":
    main()
