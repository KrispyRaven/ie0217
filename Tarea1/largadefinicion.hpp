#ifndef LARGADEFINICION_H
#define LARGADEFINICION_H
#include "definicion.hpp"
#include <iostream>
#include <string>
#include <vector>

using namespace std;


class largaDefinicion : public Definicion {

    public:
    string ldefinicion;

    largaDefinicion(int n, string preg, string def_c, string def_l) : Definicion(n , preg, def_c) , ldefinicion(def_l){}

    void mostrarInformacion();

};


#endif