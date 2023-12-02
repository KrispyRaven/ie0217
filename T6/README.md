# Precio de las casas con respecto a su tamaño u numero de habitaciones

## Como correr el programa

Abre la terminal.
Navega al directorio donde se encuentra tu archivo Python con cd (por ejemplo, cd /ruta/hacia/tu/archivo).
Ejecuta el archivo Python usando el intérprete de Python. Por ejemplo:

'python tu_archivo.py'

O si tienes Python 3.x:

'python3 tu_archivo.py'

## Datos Recolectados

Los datos se obtuvieron atravez de kaggle, la idea de este es comprobar una hipotesis de que el precio de las casas estan influenciados por su tamaño y numero de habitaciones. 

Debido a la correcta eleccion no fue necesario limpiar el dataset. Nada mas fue necesario delimitar las columnas del dataset por las de interes.

## Clusterizacion

De buenas a primeras solo se reconocian 3 cluster, pero usando el metodo de la silueta se logra determinar que son 6 los necesarios. Los cuales ya graficados con una distincion de color es bastante mas sencillo distinguirlos. El patron mas notable es cuando da un salto entre la cantidad de habitaciones o el rango de precios

## Regresion

Observando la regresion podemos denotar que en la prediccion si nos forma una relacion lineal entre el area, la cantidad de habitaciones y su precio. Que su precio va en aumento si las demas tambien aumentan.
