#Se definen los libros de la biblioteca
libros_disponibles = [
    {"titulo": "El Gran Gatsby", "autor": "F. Scott Fitzgerald", "prestado": False},
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "prestado": False},
    {"titulo": "1984", "autor": "George Orwell", "prestado": False}
]

#Funcio
def mostrar_libros_disponibles():
    print("Libros disponibles:")
    for i, libro in enumerate(libros_disponibles):
        estado = "Disponible" if not libro["prestado"] else "Prestado"
        print(f"{i + 1}. {libro['titulo']} de {libro['autor']} - {estado}")

def prestar_libro(usuario, libro_idx):
    if 0 <= libro_idx < len(libros_disponibles) and not libros_disponibles[libro_idx]["prestado"]:
        libros_disponibles[libro_idx]["prestado"] = True
        print(f"El libro '{libros_disponibles[libro_idx]['titulo']}' ha sido prestado a {usuario}.")
    else:
        print("El libro no está disponible para préstamo.")

def biblioteca():
    print("¡Bienvenido a la Biblioteca!")

    while True:
        print("\n¿Qué te gustaría hacer?")
        print("1. Mostrar libros disponibles")
        print("2. Tomar prestado un libro")
        print("3. Salir")

        opcion = input("Elije una opción: ")

        if opcion == "1":
            mostrar_libros_disponibles()
        elif opcion == "2":
            usuario = input("Ingresa tu nombre: ")
            mostrar_libros_disponibles()
            libro_idx = int(input("Ingresa el número del libro que deseas tomar prestado: ")) - 1
            prestar_libro(usuario, libro_idx)
        elif opcion == "3":
            print("Gracias por usar la biblioteca. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

biblioteca()
