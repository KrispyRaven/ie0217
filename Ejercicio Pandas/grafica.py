import pandas as pd
import matplotlib.pyplot as plt
personas_df = pd.read_csv("personas.csv")

# inciso 1

# Crear un histograma de edades
input()
plt.hist(personas_df['Edad'], color='red')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.title('Histograma de Edades')
plt.grid(True)

# Mostrar el histograma
plt.show()

#inciso 2
input()
# Calcular la cantidad de hombres y mujeres# Calcular la cantidad de hombres y mujeres
conteo_genero = personas_df['Sexo'].value_counts()

# Crear un diagrama de barras
conteo_genero.plot(kind='bar', color=['lightblue', 'lightpink'])
plt.xlabel('Sexo')
plt.ylabel('Cantidad')
plt.title('Distribución por Sexo')
plt.xticks(rotation=0)  # Para que las etiquetas en el eje x no estén giradas
plt.show()

# inciso 3
input()

# Calcular la cantidad de hombres y mujeres# Calcular la cantidad de hombres y mujeres# Calcular la cantidad de personas en cada grupo
conteo_grupos = personas_df['Grupo'].value_counts()

# Crear un diagrama de barras de grupo
conteo_grupos.plot(kind='bar', color='lightgreen')
plt.xlabel('Grupo')
plt.ylabel('Cantidad de Personas')
plt.title('Distribución por Grupo')
plt.xticks(rotation=0)  # Para que las etiquetas en el eje x no estén giradas
plt.show()

#inciso 4

input()
# Crear un diagrama de dispersión de altura vs. peso
plt.figure(figsize=(8, 6))  # Opcional: ajusta el tamaño del gráfico
plt.scatter(personas_df['Altura (cm)'], personas_df['Peso (kg)'], color='blue', alpha=0.5)
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Diagrama de Dispersión de Altura vs. Peso')
plt.grid(True)
plt.show()

# inciso 5
input()
plt.figure(figsize=(10, 6))  # Opcional: ajusta el tamaño del gráfico
for i in range(len(personas_df)):
    persona = personas_df.loc[i]
    plt.plot(['Puntaje1', 'Puntaje2', 'Puntaje3'], [persona['Puntaje1'], persona['Puntaje2'], persona['Puntaje3']], label=f'Persona {i+1}')

plt.xlabel('Puntajes')
plt.ylabel('Valor')
plt.title('Evolución de Puntajes')
plt.legend()
plt.grid(True)
plt.show()

# inciso 6
input() 
# Crear un gráfico de cajas de puntajes por grupo
plt.figure(figsize=(10, 6))  # Opcional: ajusta el tamaño del gráfico
personas_df.boxplot(column=['Puntaje1', 'Puntaje2', 'Puntaje3'], by='Grupo', grid=False)

plt.xlabel('Grupo')
plt.ylabel('Puntaje')
plt.title('Gráfico de Cajas de Puntajes por Grupo')
plt.suptitle('')  # Suprimir el título automático generado por boxplot

plt.show()

#inciso 7
input()

# Calcular la cantidad de personas en cada grupo# Agrupar los datos por género y calcular la suma de los puntajes
puntajes_por_genero = personas_df.groupby('Sexo')[['Puntaje1', 'Puntaje2', 'Puntaje3']].sum()

# Crear un diagrama de barras apiladas
plt.figure(figsize=(10, 6))  # Opcional: ajusta el tamaño del gráfico
puntajes_por_genero.plot(kind='bar', stacked=True)
plt.xlabel('Sexo')
plt.ylabel('Suma de Puntajes')
plt.title('Diagrama de Barras Apiladas de Puntajes por Género')
plt.xticks(rotation=0)  # Para que las etiquetas en el eje x no estén giradas
plt.legend(title='Puntaje', loc='upper right')
plt.show()