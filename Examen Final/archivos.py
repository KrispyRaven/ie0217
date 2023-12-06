import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Item 5
dataframe = pd.read_csv('conjunto_datos11931799.csv')

filas_mayores_30 = dataframe[dataframe['Edad'] > 30]
print(filas_mayores_30)

# Item 6
plt.figure(figsize=(8, 6))  # Tamaño del gráfico
plt.scatter(dataframe['Altura'], dataframe['Peso'], color='blue', alpha=0.5)
plt.title('Relación entre Altura y Peso')  # Título del gráfico
plt.xlabel('Altura')  # Etiqueta del eje x
plt.ylabel('Peso')  # Etiqueta del eje y
plt.show()  # Mostrar el gráfic

# Item 7

X = dataframe[['Edad']]  # Variable independiente (predictor)
y = dataframe['Peso']  # Variable dependiente (objetivo)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=42)

# Crear y entrenar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Realizar predicciones con el conjunto de prueba
predicciones = modelo.predict(X_test)

# Graficar la regresión lineal
plt.figure(figsize=(8, 6))

# Graficar datos reales
plt.scatter(X, y, color='blue', label='Datos reales')

# Graficar la regresión lineal
plt.plot(X_test, predicciones, color='red', label='Regresión lineal')
plt.title('Regresión Lineal: Altura vs Peso')
plt.xlabel('Altura')
plt.ylabel('Peso')
plt.legend()
plt.grid(True)
plt.show()


# Item 8

# Seleccionar características relevantes para el clustering
features = dataframe[['Edad', 'Altura', 'Peso']]


scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Aplicar el algoritmo de K-Means para agrupar a las personas en k clústeres
k = 3  # Número de clústeres (puedes ajustar este valor)
kmeans = KMeans(n_clusters=k, random_state=42)
dataframe['Cluster'] = kmeans.fit_predict(features_scaled)

# Visualizar los clústeres en un gráfico 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(features_scaled[:, 0], features_scaled[:, 1], features_scaled[:, 2],
           c=dataframe['Cluster'], cmap='viridis')
ax.set_xlabel('Edad')
ax.set_ylabel('Altura')
ax.set_zlabel('Peso')
ax.set_title('Clustering de Personas')

plt.show()
