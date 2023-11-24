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

# Iterar para diferentes números de clusters
for n_clusters in range(2, 20):  # por ejemplo, de 2 a 20 clusters
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(X_scaled)
    
    # Calcular la puntuación de la silueta
    silhouette_avg = silhouette_score(X_scaled, cluster_labels)
    print(f"For n_clusters={n_clusters}, the average silhouette score is: {silhouette_avg:.4f}")