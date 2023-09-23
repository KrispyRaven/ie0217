#include <iostream>
#include <string>
#include <vector>
#include "angulo.hpp"
#include "serial.hpp"
#include "barco.hpp"
#include <chrono>

using namespace std;

// Funcion para comparar dos Barcos por su latitud (Norte a Sur)
bool compararLatitud(const Barco &a, const Barco &b) {
    string N = "N";
    string S = "S";
    if (a.latitud.direccion == N && b.latitud.direccion == S) return true;
    if (a.latitud.direccion == S && b.latitud.direccion == N) return false;
    // En el caso de latitudes iguales, compara los grados y minutos
    if (a.latitud.grados == b.latitud.grados) return a.latitud.minutos < b.latitud.minutos;
    return a.latitud.grados < b.latitud.grados;
}

// Implementacion del algoritmo QuickSort con contador
int quickSort(vector<Barco> &Barcos, int izquierda, int derecha) {
    int comparaciones = 0;
    if (izquierda < derecha) {
        cout << "inicio, pivote" << endl;
        Barco pivote = Barcos[derecha];
        cout << "fin, pivote" << endl;

        int i = izquierda - 1;

        for (int j = izquierda; j <= derecha - 1; j++) {
            comparaciones++;
            if (compararLatitud(Barcos[j], pivote)) {
                i++;
                swap(Barcos[i], Barcos[j]);
            }
        }

        swap(Barcos[i + 1], Barcos[derecha]);
        int puntoDeParticion = i + 1;

        comparaciones += quickSort(Barcos, izquierda, puntoDeParticion - 1);
        comparaciones += quickSort(Barcos, puntoDeParticion + 1, derecha);
    }
    return comparaciones;
}

// Implementacion del algoritmo MergeSort con contador, solo que la implementacion no se concreto por necesitar un pivote y este generar nuevos registros
int merge(vector<Barco> &Barcos, int izquierda, int medio, int derecha) {
    int comparaciones = 0;
    int n1 = medio - izquierda + 1;
    int n2 = derecha - medio;

    cout << "Inicio izqder" << endl;
    vector<Barco> izq(n1), der(n2);
    cout << "Fin izqder" << endl;

    for (int i = 0; i < n1; i++) izq[i] = Barcos[izquierda + i];
    for (int i = 0; i < n2; i++) der[i] = Barcos[medio + 1 + i];

    int i = 0, j = 0, k = izquierda;

    while (i < n1 && j < n2) {
        comparaciones++;
        if (compararLatitud(izq[i], der[j])) {
            Barcos[k] = izq[i];
            i++;
        } else {
            Barcos[k] = der[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        Barcos[k] = izq[i];
        i++;
        k++;
    }

    while (j < n2) {
        Barcos[k] = der[j];
        j++;
        k++;
    }

    return comparaciones;
}

int mergeSort(vector<Barco> &Barcos, int izquierda, int derecha) {
    int comparaciones = 0;
    if (izquierda < derecha) {
        int medio = izquierda + (derecha - izquierda) / 2;

        comparaciones += mergeSort(Barcos, izquierda, medio);
        comparaciones += mergeSort(Barcos, medio + 1, derecha);

        comparaciones += merge(Barcos, izquierda, medio, derecha);
    }
    return comparaciones;
}


// Implementacion del algoritmo SelectionSort con contador
int seleccionSort(vector<Barco> &angulos) {
    int n = angulos.size();
    int comparaciones = 0;

    for (int i = 0; i < n - 1; i++) {
        int minimo = i;
        for (int j = i + 1; j < n; j++) {
            comparaciones++;
            if (compararLatitud(angulos[j], angulos[minimo])) {
                minimo = j;
            }
        }
        if (minimo != i) {
            swap(angulos[i], angulos[minimo]);
        }
    }
    return comparaciones;
}