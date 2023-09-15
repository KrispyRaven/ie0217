#ifndef BARCO_H
#define BARCO_H
#include <iostream>
#include <string>
#include "angulo.hpp"
#include "serial.hpp"

using namespace std;

class Barco{

    public:
    Serial barcoSerial;
    Angulo latitud;
    Angulo longitud;

    Barco(int gradosLatitud = 0, float minutosLatitud = 0.0,  string direccionLatitud = "N", int gradosLongitud = 0, float minutosLongitud = 0.0,  string direccionLongitud = "N"): latitud(gradosLatitud,minutosLatitud,direccionLatitud), longitud(gradosLongitud,minutosLongitud,direccionLongitud){};


    void agregarValores();

    void mostrarBarco();

};



#endif