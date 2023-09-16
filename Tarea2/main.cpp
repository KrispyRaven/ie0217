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

        cout << "Menú principal:\n1. Añadir un nuevo barco a la flota\n2. Eliminar un barco de la flota\n3. Mostrar la flota ordenada por latitud\n4. Salir" << endl;
        cin >> opcion;

    

        switch (opcion)
        {
        case 1:
            set.push_back(Barco());
            set[set.size()-1].agregarValores();
            break;

        case 2:
            int indice;
            cout <<  "Brinde el numero de serie del Barco a eliminar:" << endl;
            cin >> indice;
            for (size_t i = 0; i < set.size(); ++i)
            {
                if (set[i].barcoSerial.mostrarSerial() == indice )
                {
                    cout << "Se procede a borrar el Barco";
                    set.erase(set.begin() + i);
                }
                
            }
            

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