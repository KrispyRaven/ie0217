
#include <iostream>
#include <string>
#include "angulo.hpp"
#include "serial.hpp"
#include "barco.hpp"

using namespace std;

void Barco::agregarValores(){
    cout << "Ingrese la latitud del barco:" << endl;
    cout << "Grados:" << endl;
    cin >> latitud.grados;
    cout << "Minutos:" << endl;
    cin >> latitud.minutos;
    cout << "Dirección (N/S):" << endl;
    cin  >> latitud.direccion;
    cout << "Ingrese la longitud del barco:" << endl;
    cout << "Grados:" << endl; 
    cin >> longitud.grados;
    cout << "Minutos:" << endl;
    cin >> longitud.minutos;
    cout << "Dirección (E/W):" << endl;
    cin >> longitud.direccion;


}

void Barco::mostrarBarco(){
    
    cout << "Barco numero de serie: " << barcoSerial.mostrarSerial();
    cout << endl;

    cout << "Latitud:";
    latitud.mostrarAngulo();

    cout << "longitud";
    longitud.mostrarAngulo();

}

