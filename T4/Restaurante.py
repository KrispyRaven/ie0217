class Restaurante:
    """"Clase Restaurante"""

    def __init__(self, nombre="", tipoCocina=""):
        self.__nombre = nombre
        self.__tipoCocina = tipoCocina

    def setNombre(self, textoIn):
        self.__nombre = textoIn

    def getNombre(self):
        print(self.__nombre)

    def setTipoCocina(self, textoIn):
        self.__tipoCocina = textoIn

    def getTipoCocina(self):
        print(self.__tipoCocina)


class MenuTematicos(Restaurante):
    """"Clase de menus tematicos del restaurante"""

    def __init__(self, nombre="", tipoCocina="", tipoMenu=""):
        self.tipoMenu = tipoMenu
        super().__init__(nombre, tipoCocina)


class HeladosCacique(MenuTematicos):
    """"Clase que incluye los helados de los menus tematicos"""

    def __init__(self, nombre="", tipoCocina="",
                 tipoMenu="", listaSabores=list()):
        self.listaDeSabores = listaSabores
        super().__init__(nombre, tipoCocina, tipoMenu)

    def __add__(self, other):
        self.listaDeSabores.append(other)
        return "Sabor guardado con exito"

    def mostrarSabores(self):
        print("\n".join(map(str, self.listaDeSabores)))

