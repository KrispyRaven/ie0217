#ifndef ANGULO_H
#define ANGULO_H
#include <iostream>
#include <string>


using namespace std;

class Angulo {

    public:

    int grados;
    float minutos;
    string direccion; 

    Angulo(int g = 0, float m = 0.0, string d = "N") : grados(g) , minutos(m) , direccion(d){}

    void mostrarAngulo();

};

#endif