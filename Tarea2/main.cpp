#include "angulo.hpp"
#include "serial.hpp"
#include "barco.hpp"
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int Serial::contador = 0;


int main() {
    bool Repetir = true;
    int opcion;
    vector <Barco> set;


    do
    {
        Barco temp;
        cout << "Menú principal:\n1. Añadir un nuevo barco a la flota\n2. Eliminar un barco de la flota\n3. Mostrar la flota ordenada por latitud\n4. Salir" << endl;
        cin >> opcion;

        switch (opcion)
        {
        case 1:

            temp.agregarValores();
            set.push_back(temp);
            break;

        case 2:
            cout << "2" << endl;
            break;

        case 3:
            for (size_t i = 0; i < set.size(); ++i)
            {
                set[i].mostrarBarco();
            }
            
            break;

        case 4:
            
            Repetir = false;
            break;
                                
        default:
            break;
        }

    } while (Repetir);
    





    return 0;
}