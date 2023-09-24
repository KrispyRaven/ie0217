# Tarea 2
## Noel Blandon
Para ejecutar vaya a al directorio de la Tarea y ejecute los siguientes comandos
_"g++ -o .\build\prueba.exe .\src\main.cpp .\src\angulo.cpp .\src\serial.cpp .\src\barco.cpp .\src\funcion.cpp"_ Y despues ejecute
_".\build\prueba.exe"_

Relación entre la eficiencia medida en tiempo y pasos
========
### Quicksort



#### Eficiencia en Tiempo: 
QuickSort es un algoritmo de ordenación muy eficiente en términos de tiempo en promedio. Su complejidad promedio es O(n log n), lo que significa que su tiempo de ejecución aumenta de manera logarítmica con el tamaño de la entrada. Esto hace que QuickSort sea una excelente opción para grandes conjuntos de datos. 

#### Eficiencia Programática: 
En términos del número de comparaciones y asignaciones, QuickSort puede realizar menos pasos en comparación con algoritmos de ordenación más simples como BubbleSort o SelectionSort. Sin embargo, el número de pasos puede variar según la elección del pivote y la distribución de los datos. En el peor caso, QuickSort puede tener una complejidad de O(n^2) si se elige un pivote malo, pero este caso rara vez se presenta en la práctica

### SelectionSort



#### Eficiencia en Tiempo: 
SelectionSort es un algoritmo de ordenación simple pero no eficiente en términos de tiempo. Su complejidad es O(n^2), lo que significa que su tiempo de ejecución aumenta cuadráticamente con el tamaño de la entrada. Esto hace que SelectionSort sea poco práctico para grandes conjuntos de datos. 

#### Eficiencia Programática: 
En términos de pasos, SelectionSort realiza un número constante de comparaciones (n * (n-1)/2) y un número lineal de intercambios (n-1). Esto lo hace fácil de entender y programar. Sin embargo, su rendimiento es pobre en comparación con algoritmos de ordenación más eficientes como QuickSort.


## Demostracion en el codigo:

Este código mide el tiempo de ejecución y el número de comparaciones (pasos) para SelectionSort y QuickSort. Para esto se empleo los siguientes comandos para medir el tiempo 
~~~c++
#include <chrono>

auto start1 = chrono::system_clock::now();
funcion_ejemplo();
auto end1 = chrono::system_clock::now();

chrono::duration<float, milli> duration1 = end1 - start1;
~~~

Este fragmento de codigo captura el tiempo antes de ejecutar la funcion y despues de ejecutarla, despues de esto se hace una resta para calcular la ejecucion del mismo. 

Para el caso de ver la cantidad de comparaciones que se realizaon lo unico que se hace es colocar una variable que se autosume cada vez que se haga una comparacion de valores para ver si uno es mayor que otro.

Dando que en la mayoria de casos que QuickSort es considerablemente más rápido y realiza menos pasos en comparación con SelectionSort para el mismo conjunto de datos. Esto demuestra la diferencia en la eficiencia entre estos dos algoritmos.


## Bibliografia

[QuickSort](https://www.programiz.com/dsa/selection-sort#google_vignette)

[SelectionSort](https://www.programiz.com/dsa/quick-sort)