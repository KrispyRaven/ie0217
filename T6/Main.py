import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("Housing.csv")



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


#Calcular el coeficiente de cluster por el metodo de la silueta

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

#######################################################################################
#Generacion del Cluster

# Crear un modelo KMeans con 6 clusters
kmeans = KMeans(n_clusters=6, random_state=42)

# Ajustar el modelo a los datos y obtener las etiquetas de los clusters
cluster_labels = kmeans.fit_predict(X_scaled)

# Crear una figura 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar los puntos de datos con colores según los clusters
scatter = ax.scatter(X_scaled[:, 0], X_scaled[:, 1], X_scaled[:, 2], c=cluster_labels, cmap='viridis', s=50)
ax.set_xlabel('Price')
ax.set_ylabel('Area')
ax.set_zlabel('Bedrooms')

# Agregar leyenda para los clusters
legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
ax.add_artist(legend1)

plt.title('Clustering de datos en 3D')
plt.show()