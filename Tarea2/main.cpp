#include "angulo.hpp"
#include "serial.hpp"
#include "barco.hpp"
#include <iostream>
#include <string>


using namespace std;

int Serial::contador = 0;

int main() {


    for (int i = 0;i<6 ;i++){
        
        Barco b1;
        
        b1.agregarValores();
        b1.mostrarBarco();


        

    }





    return 0;
}