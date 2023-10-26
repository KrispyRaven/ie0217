class Restaurante:
    """"Clase Restaurante"""

# Constructor de la clase
    def __init__(self, nombre="", tipoCocina=""):
        self.__nombre = nombre
        self.__tipoCocina = tipoCocina

# Setter del atributo Nombre
    def setNombre(self, textoIn):
        self.__nombre = textoIn

# Getter del atributo nombre
    def getNombre(self):
        print(self.__nombre)

# Setter del atributo tipo de Cocina 
    def setTipoCocina(self, textoIn):
        self.__tipoCocina = textoIn

# Getter del atributo tipo de Cocina
    def getTipoCocina(self):
        print(self.__tipoCocina)


class MenuTematicos(Restaurante):
    """"Clase de menus tematicos del restaurante"""

# Constructor de la clase
    def __init__(self, nombre="", tipoCocina="", tipoMenu=""):
        self.tipoMenu = tipoMenu
        super().__init__(nombre, tipoCocina)


class HeladosCacique(MenuTematicos):
    """"Clase que incluye los helados de los menus tematicos"""

# Constructor de la clase
    def __init__(self, nombre="", tipoCocina="",
                 tipoMenu="", listaSabores=list()):
        self.listaDeSabores = listaSabores
        super().__init__(nombre, tipoCocina, tipoMenu)

# Metodo agregar sabores a la lista utilizando el operador "+"
    def __add__(self, other):
        self.listaDeSabores.append(other)
        return "Sabor guardado con exito"

# Metodo para mostrar los sabores de la lista
    def mostrarSabores(self):
        print("\n".join(map(str, self.listaDeSabores)))
