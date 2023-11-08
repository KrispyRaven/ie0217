import pandas as pd

ventas_df = pd.read_csv("ventas.csv")

# print(ventas_df.sample(10))

# inciso 1
total_ventas = ventas_df.groupby("Producto")["Total"].sum()

input()
print(total_ventas)
print("-----------------.------------------")

# inciso 2
mas_vendido = ventas_df.groupby("Producto")["Cantidad"].sum().idxmax()
input()
print("El producto más vendido en términos de cantidad es:", mas_vendido)
print("-----------------.------------------")

# inciso 3

total_cantidad = ventas_df.groupby("Producto")['Cantidad'].sum()
total_total = ventas_df.groupby("Producto")['Total'].sum()

promedio = total_total/total_cantidad
input()
print(promedio)
print("-----------------.------------------")

# inciso 4

venta_mayor_ingresos = ventas_df[ventas_df['Total'] == ventas_df['Total'].max()]

# Extraer la fecha correspondiente
fecha_mayor_ingresos = venta_mayor_ingresos['Fecha'].values[0]

# Imprimir la fecha
input()
print("La venta de mayor valor en términos de ingresos se realizó en la fecha", fecha_mayor_ingresos)
print("-----------------.------------------")

# inciso 5

# Asegúrate de que la columna "fecha" sea de tipo datetime
ventas_df['Fecha'] = pd.to_datetime(ventas_df['Fecha'])

# Filtrar las ventas del último trimestre (octubre, noviembre y diciembre)
ultimo_trimestre_ventas = ventas_df[(ventas_df['Fecha'].dt.month >= 10) & (ventas_df['Fecha'].dt.month <= 12)]

# Imprimir el resultado
input()
print("Ventas realizadas en el último trimestre del año:", ultimo_trimestre_ventas)
print("-----------------.------------------")

# inciso 6

nuevo_df = ventas_df[["Fecha", "Producto", "Cantidad"]]
input()
print(nuevo_df)

# inciso 7

nuevo_df.to_csv('ventas_trimestre.csv', index=False)
input()
print("El nuevo DataFrame se ha guardado en 'ventas_trimestre.csv'.")