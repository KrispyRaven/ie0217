'''Este es un diccionario que representa los libros disponibles en la biblioteca. 
Cada diccionario contiene tres claves: "titulo" (el título del libro), "autor" (el autor del libro) y "prestado" (un valor booleano que indica si el libro ha sido prestado o no).'''
libros_disponibles = [
    {"titulo": "El Gran Gatsby", "autor": "F. Scott Fitzgerald", "prestado": False},
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "prestado": False},
    {"titulo": "1984", "autor": "George Orwell", "prestado": False}
]

'''
Esta función muestra en la consola una lista de los libros disponibles junto con su estado (Disponible o Prestado). 
Itera a través de la lista libros_disponibles y muestra información sobre cada libro.
'''
def mostrar_libros_disponibles():
    print("Libros disponibles:")
    #For para iterar entre los libros de las lista
    for i, libro in enumerate(libros_disponibles):
        
        #Aca verificamos y definimos la variable estado, Empleando un if para verificamos si el libro tiene su boolenao true o false para definir si esta disponible o no.
        estado = "Disponible" if not libro["prestado"] else "Prestado"
        
        #Print que brinda el indice en la primera expresion empleando la variable de iteracion del for y ademas da los atributos de titulo, autor y estado
        print(f"{i + 1}. {libro['titulo']} de {libro['autor']} - {estado}")


''' 
La función permite prestar un libro a un usuario tomando dos argumentos, el nombre del usuario que solicita el préstamo y el índice del libro en el diccionario. 
Verifica si el índice proporcionado es válido y si el libro no está prestado. 
Si se cumplen estas condiciones, el libro pone su booleano en true para indica que esta prestado y muestra un mensaje confirmando el préstamo. 
Si el libro no está disponible para préstamo, muestra un mensaje informandolo.
'''
def prestar_libro(usuario, libro_idx):
    if 0 <= libro_idx < len(libros_disponibles) and not libros_disponibles[libro_idx]["prestado"]:
        libros_disponibles[libro_idx]["prestado"] = True
        print(f"El libro '{libros_disponibles[libro_idx]['titulo']}' ha sido prestado a {usuario}.")
    else:
        print("El libro no está disponible para préstamo.")

'''
Esta funcion nos crea la biblioteca. Ademas nos llama a las funciones creadaas anteriormente para hacer la implementacion de estas mediante un menu
'''
def biblioteca():
    print("¡Bienvenido a la Biblioteca!")

    #Inicio de while para tener un loop en el menu
    while True:
        #Opciones del menu
        print("\n¿Qué te gustaría hacer?")
        print("1. Mostrar libros disponibles")
        print("2. Tomar prestado un libro")
        print("3. Salir")

        #Ingreso de la opcion
        opcion = input("Elije una opción: ")

        #Operador de comparacion para entrar a unas de las opciones del menu con la variable de ingreso opcion. Este va ir recorriendo los if hasta encontrar el que satisface la condicion de igualdal
        if opcion == "1":
            mostrar_libros_disponibles()
        elif opcion == "2":
            usuario = input("Ingresa tu nombre: ")
            mostrar_libros_disponibles()
            libro_idx = int(input("Ingresa el número del libro que deseas tomar prestado: ")) - 1
            prestar_libro(usuario, libro_idx)
        elif opcion == "3":
            print("Gracias por usar la biblioteca. ¡Hasta luego!")
            #El break detiene el loop del while
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

#Funcion para iniciar la biblioteca.
biblioteca()
