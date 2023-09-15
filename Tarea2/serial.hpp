#ifndef SERIAL_H
#define SERIAL_H
#include <iostream>
#include <string>


using namespace std;

class Serial {

    public:
    static int contador; // Variable estática para mantener un conteo de objetos
    int numeroDeSerie;

    Serial(){

        contador++;
        numeroDeSerie = contador;

    }

    int mostrarSerial();

};

#endif