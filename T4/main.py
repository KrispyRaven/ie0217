import Restaurante

R1 = Restaurante.HeladosCacique()
BarNombre = input("Digite el nombre del bar:")
Cocina = input("\nIngresee el tipo de cocina:")

R1.setNombre(BarNombre)
R1.setTipoCocina(Cocina)

print("\nRestuarante agregado con exito")

print("\nEl nombre del Bar es:")
R1.getNombre()

print("\nEl tipo de cocina del bar es:")
R1.getTipoCocina()

respuesta = ''
while respuesta not in ['s', 'n']:
    respuesta = input("Por favor, ingrese s o n: ").upper()
    if respuesta not in ['S', 'N']:
        print("Respuesta no válida. Inténtelo de nuevo.")

print("El bucle se detuvo. La respuesta es:", respuesta)


MenuTematico = input("\nIngrese el nombre del menu tematico:")
R1.tipoMenu = MenuTematico
print("\nEL tipo de menu es:\n", R1.tipoMenu)
 
loopMenu = True

while loopMenu:
    pass