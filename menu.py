# ------------------------------------------------------------
# menu.py
# Este archivo contiene el menú principal del programa.
# Desde aquí el usuario puede elegir opciones para agregar
# personas, mostrarlas o salir del programa.
# ------------------------------------------------------------

from gestionpersonas import GestorPersonas   # Importamos la clase que gestiona las personas

def main()  :
    # Creamos una instancia del gestor, que se encargará de guardar y manejar las personas
    gestor = GestorPersonas()

    # Bucle principal que mantiene el menú funcionando
    
    while True:
        print(" Menú Principal ")
        print("1. Agregar persona")
        print("2. Mostrar personas")
        print("3. Eliminar persona")
        print("4. Modificar persona")
        print("5. Salir")

        # Solicitamos al usuario que elija una opción
        opcion = input("Seleccione una opcion: ")

        # Si elige agregar persona
        if opcion == "1":
            # Pedimos al usuario la información necesaria
            nombre = input("Nombre   : ")
            apellido = input("Apellido: ")
            edad = input("Edad: ")
            documento = input("Documento: ")
            gmail = input("Gmail: ")
            lugar_vive = input("Lugar donde vive: ")

            # Llamamos al método del gestor para crear y almacenar la persona
            gestor.agregar_persona(nombre, apellido, edad, documento, gmail, lugar_vive)

        # Si elige mostrar las personas registradas
        elif opcion == "2":
            gestor.mostrar_personas()

          # Eliminar persona
        elif opcion == "3":
            doc = input("Ingrese el documento de la persona a eliminar: ")
            gestor.eliminar_persona(doc)

        # Modificar persona
        elif opcion == "4":
            doc = input("Ingrese el documento de la persona a modificar: ")
            gestor.modificar_persona(doc) 

        # Salir
        elif opcion == "5":
            print("Saliendo del programa...")
            break       

        # Si escribe algo que no es válido
        else:
            print("Opción no válida, intente nuevamente.")

# Punto de inicio del programa
if __name__ == "__main__":
    main()
