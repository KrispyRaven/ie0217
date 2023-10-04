#include <iostream>
#include <string>
#include "student.hpp"

using namespace std;



int main() {

    // Inicializacion de Variables
    string nombre;
    float calificacion;
    bool repetir = true;
    
    do
    {
            //Puesta en marcha el control de excepciones
        try {

            // Ingreso de las variables por parte del usuario
            cout << "Ingrese el nombre del estudiante: ";
            cin >> nombre;

            cout << "Ingrese la calificación del estudiante: ";
            cin >> calificacion;

            // Creacion del Objeto estudiante
            Estudiante estudiante(nombre, calificacion);

            // Mostrar el estudiante
            estudiante.MostrarInformacion();
        }
        catch (const invalid_argument& e) {
            cerr << "Error: " << e.what() << std::endl;
        }
        
    } while (repetir);
    

   

    return 0;
}