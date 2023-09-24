#ifndef FUNCION_H
#define FUNCION_H
#include <iostream>
#include <string>
#include <vector>
#include "angulo.hpp"
#include "serial.hpp"
#include "barco.hpp"

using namespace std;
bool compararLatitud(const Barco &a, const Barco &b);

int quickSort(vector<Barco> &Barcos, int izquierda, int derecha);

int merge(vector<Barco> &Barcos, int izquierda, int medio, int derecha);

int mergeSort(vector<Barco> &Barcos, int izquierda, int derecha);

int seleccionSort(vector<Barco> &angulos);

#endif