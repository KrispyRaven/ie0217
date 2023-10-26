# Funcion para validar las entradas dependiento del contexto y tipo de Dato
def validar_entrada(TipoDato, NombreEntrada="Algo"):

    # Inicializacion de Variables que se pueden llegar a emplear
    respuesta = ""
    respuesta1 = ""
    continuar = True

    # Escenario para evaluar la creacion del menu Tematico
    if TipoDato == "Tematico":

        """Verifica si en la entrada se revibio lo que se especifica"""

        while respuesta not in ['S']:
            respuesta = input("Por favor, ingrese S/s: ").upper()
            if respuesta not in ['S']:
                print("Respuesta no válida.\
                No puedo hacer nada si no ingresa menu tematico")

# Escenario para evaluar las si se crean nuevos elementos de la lista Helado
    if TipoDato == "Helado":

        """Verifica si en la entrada se revibio lo que se especifica"""

        while respuesta1 not in ['S', 'N']:
            respuesta1 = input("Por favor, ingrese S/s o N/n: ").upper()
            if respuesta1 not in ['S', 'N']:
                print("Respuesta no válida. Inténtelo de nuevo.")
            if respuesta1 == "N":
                print("Gracias! por usar el sistema, hasta la proxima!")

                continuar = False

                return continuar
        return continuar

    # Escenario para evaluar las entradas de los nombres
    if TipoDato == "Nombre":

        """Verifica si la entrada está vacía
        o contiene solo espacios en blanco"""

        while NombreEntrada == "":
            NombreEntrada = input("El input está vacío. Intente de nuevo:")
        return NombreEntrada
