#include "angulo.hpp"
#include "serial.hpp"
#include "barco.hpp"
#include "funcion.hpp"
#include <iostream>
#include <string>
#include <vector>
#include <chrono>

using namespace std;

int Serial::contador = 0;


int main() {

    //opciones para el menu
    bool Repetir = true;
    int opcion;

    // Creacion del set de Barcos
    vector <Barco> set;



    do
    {

        cout << "Menú principal:\n1. Añadir un nuevo barco a la flota\n2. Eliminar un barco de la flota\n3. Mostrar la flota ordenada por latitud\n4. Salir" << endl;
        cin >> opcion; 

        //Inicializacion de copias para las funciones de sort diferentes y sus comparaciones 
        vector <Barco> BQ = set;
        vector <Barco> BS = set;
        int comparacionesQS;
        int comparacionesSS;

        

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
            
            auto start1 = chrono::system_clock::now();
            comparacionesQS = quickSort(BQ, 0, BQ.size() - 1);
            auto end1 = chrono::system_clock::now();

            chrono::duration<float, milli> duration1 = end1 - start1;

            auto start2 = chrono::system_clock::now();
            comparacionesSS = seleccionSort(BS);
            auto end2 = chrono::system_clock::now();

            chrono::duration<float, milli> duration2 = end2 - start2;

            cout << "Comparaciones con QuickSort: " << comparacionesQS << "  Tiempo de ejecucion: " << duration1.count() << "ms"  << endl;
            cout << "Comparaciones con SelectionSort: " << comparacionesSS << "  Tiempo de ejecucion: " << duration2.count() << "ms"<< endl;

            cout << "Barcos como se ingresaron originalmente"  << endl;
            for (size_t i = 0; i < set.size(); i++)
            {
                set[i].mostrarBarco();
            }
            cout << "Barcos ordenados con Quick" << endl;
            for (size_t i = 0; i < BQ.size(); i++)
            {
                BQ[i].mostrarBarco();
            }
            
            cout << "Barcos ordenados con selection" << endl;
            for (size_t i = 0; i < BQ.size(); i++)
            {
                BS[i].mostrarBarco();
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