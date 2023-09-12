#ifndef DEFINICION_H
#define DEFINICION_H
#include <iostream>
#include <string>
#include <vector>

using namespace std;



class Definicion {

    public:
    int pos_number;
    string pregunta;
    string definicion;

    Definicion(int n, string preg, string def_c) : pos_number(n), pregunta(preg), definicion(def_c){}

    void mostrarInformacion();

};

#endif