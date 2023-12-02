import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("Housing.csv")


###############################################################################
#                      Generacion del Cluster                                 #
###############################################################################

# Configurar la figura y el subplot en 3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar en 3D
ax.scatter(df['area'], df['bedrooms'], df['price'], c='r', marker='o')

# Etiquetas de los ejes
ax.set_xlabel('Area')
ax.set_ylabel('Bedrooms')
ax.set_zlabel('Price')

# Mostrar el gráfico
plt.title('Price vs Area vs Bedrooms')
plt.show()


# Calcular el coeficiente de cluster por el metodo de la silueta

# Convertir los datos en un arreglo numpy
X = np.array(list(zip(df['price'], df['area'], df['bedrooms'])))

# Escalar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Lista para almacenar las puntuaciones de la silueta
silhouette_scores = []

# Iterar para diferentes números de clusters
for n_clusters in range(2, 10):  # de 2 a 10 clusters
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(X_scaled)

    # Calcular la puntuación de la silueta
    silhouette_avg = silhouette_score(X_scaled, cluster_labels)
    silhouette_scores.append(silhouette_avg)

# Graficar el método de la silueta
plt.figure(figsize=(8, 6))
plt.plot(range(2, 10), silhouette_scores, marker='o', linestyle='--')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Method')
plt.xticks(range(2, 10))
plt.grid(True)
plt.show()


# Crear un modelo KMeans con 6 clusters
kmeans = KMeans(n_clusters=6, random_state=42)

# Ajustar el modelo a los datos y obtener las etiquetas de los clusters
cluster_labels = kmeans.fit_predict(X_scaled)

# Crear una figura 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar los puntos de datos con colores según los clusters
scatter = ax.scatter(X_scaled[:, 0], X_scaled[:, 1], X_scaled[:, 2],
                     c=cluster_labels, cmap='viridis', s=50)
ax.set_xlabel('Price')
ax.set_ylabel('Area')
ax.set_zlabel('Bedrooms')

# Agregar leyenda para los clusters
legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
ax.add_artist(legend1)

plt.title('Clustering de datos en 3D')
plt.show()

##############################################################################
#                          Regresion lineal multiple                         #
##############################################################################
# Convertir los datos en un arreglo numpy
X = np.array(list(zip(df['area'], df['bedrooms'])))
y = np.array(df['price'])

# Crear un modelo de regresión lineal múltiple
model = LinearRegression()

# Ajustar el modelo a los datos
model.fit(X, y)

# Coeficientes y término independiente
print("Coeficientes:", model.coef_)
print("Término independiente:", model.intercept_)

x_train, x_test, y_train, y_test = train_test_split(
    df[["area", "bedrooms"]], df["price"],
    test_size=0.2, random_state=42)

y_pred = model.predict(x_test)

# Crear una figura 3D
fig = plt.figure(figsize=(12, 6))

# Graficar 1
ax1 = fig.add_subplot(131, projection='3d')

ax1.scatter(x_test["area"], x_test["bedrooms"],
            y_test, alpha=0.5)
ax1.set_xlabel('Area')
ax1.set_ylabel('Bedrooms')
ax1.set_zlabel('Price')

# Agregar leyenda
plt.title('Precio Verdadero vs. Area y habitaciones')


# Grafica 2
ax2 = fig.add_subplot(132, projection='3d')

ax2.scatter(x_test["area"], x_test["bedrooms"],
            y_pred, alpha=0.5)
ax2.set_xlabel('Area')
ax2.set_ylabel('Bedrooms')
ax2.set_zlabel('Price Predicted')

# Agregar leyenda
plt.title('Precio predicho vs. Area y habitaciones')


# Grafica 3
ax3 = fig.add_subplot(133)

ax3.scatter(y_test, y_pred, alpha=0.5)
ax3.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)],
         linestyle="--", color="red", linewidth=2)
ax3.set_xlabel('Precio Verdadero')
ax3.set_ylabel('Precio Predicho')

# Agregar leyenda
plt.title('Comparacion de Precio Verdadero y Precio Predicho')

plt.tight_layout()
plt.show()


# Calcular R^2 usando el método score() del modelo
r2_train = model.score(x_train, y_train)
r2_test = model.score(x_test, y_test)

print(f"Coeficiente de determinación R² para el \
      conjunto de entrenamiento:{r2_train:.4f}")
print(f"Coeficiente de determinación R² para el \
      conjunto de prueba:{r2_test:.4f}")
