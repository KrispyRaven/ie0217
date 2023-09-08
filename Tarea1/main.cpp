
#include "function.hpp"
#include <iostream>

using namespace std;



int main() {

int opcion;
    bool repetir = true;
    
    do {

        
        // Texto del menú que se verá cada vez
        cout << "\n\nMenu de Opciones" << endl;
        cout << "1. Mostrar todas las definiciones almacenadas." << endl;
        cout << "2. Hacer una pregunta" << endl;
        cout << "0. SALIR" << endl;
        
        cout << "\nIngrese una opcion: ";
        cin >> opcion;
        
        switch (opcion) {
            case 1:
                // Lista de instrucciones de la opción 1                
                
                cout << "caso #1" << endl;
                break;
                
            case 2:
                // Lista de instrucciones de la opción 2                
                
                cout << "caso #2" << endl;
                break;

            
            case 0:
            	repetir = false;
            	break;
        }        
    } while (repetir);
	 
    return 0;

}