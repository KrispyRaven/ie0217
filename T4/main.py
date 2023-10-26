import Restaurante
from Validar import validar_entrada

# Se inicializa el objeto
R1 = Restaurante.HeladosCacique()

# Se piden sus atributos y se validan las entradas
BarNombre = input("Digite el nombre del bar:")
BarNombre = validar_entrada("Nombre", BarNombre)

# Se piden sus atributos y se validan las entradas
Cocina = input("\nIngresee el tipo de cocina:")
Cocina = validar_entrada("Nombre", Cocina)

R1.setNombre(BarNombre)
R1.setTipoCocina(Cocina)

print("\nRestuarante agregado con exito")

print("\nEl nombre del Bar es:")
R1.getNombre()

print("\nEl tipo de cocina del bar es:")
R1.getTipoCocina()

# Se prosigue con el menu tematico y validacion
print("\nDesea agregar un menu tematico?")

validar_entrada("Tematico")

# Se prosigue a validar la entrada y se almacena
MenuTematico = input("\nIngrese el nombre del menu tematico:")
MenuTematico = validar_entrada("Nombre", MenuTematico)
R1.tipoMenu = MenuTematico
print("\nMenu registrado! EL tipo de menu es:\n", R1.tipoMenu)


# Se crea el menu de los sabores de helado con un loop para detenerlo
continuar = True
while continuar:
    print("\nDesea agregar un sabor de helado de Cacique?")

    respuesta1 = ''
    # Valida y almacena temporalmente el sabor de helado
    continuar = validar_entrada("Helado")
    if continuar is False:
        break
    NSabor = input("Ingrese el sabor:")
    NSabor = validar_entrada("Nombre", NSabor)

    # Se agrega el sabor a la lista y imprime los disponibles
    x = R1 + NSabor
    print(x)
    print("\nSabores Disponibles")
    R1.mostrarSabores()
