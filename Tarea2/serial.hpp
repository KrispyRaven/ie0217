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

        contador = contador + 1;
        numeroDeSerie = contador;
        cout << "SE EJECUTO ESTA MIEEEEERDAAAA" << endl;
    }

    int mostrarSerial();

};

#endif