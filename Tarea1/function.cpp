#include "function.hpp"
#include "largadefinicion.hpp"
#include <iostream>
#include <string>
#include <vector>

using namespace std;









// Funcion de busqueda de strings e imprime si hay coincidencia
bool str_search(string strsearch, string strlocation, int k)
{
    int n = strsearch.length(); // longitud del parrafo
    int m = strlocation.length(); // longitud de la palabra
    if (k < n - m + 1) // Comprobar tamaño
    {
        if (strsearch.substr(k, m) == strlocation) // Busca si hay coincidencia
        {


            return true; //hay coincidencia 

        }
        else // No hay coincidencia
        {
            return str_search(strsearch, strlocation, k + 1); // Llama recursivamente la funcion con el siguiente indice
        }
    }
    else // Si no existe coincidencia del todo
    {

        return false; // return false
    }
}



//Funcion que hace el recorrido de la funcion search en un vector 
void vsearch(vector <largaDefinicion> set ){

    int posv;
    string palabra;
    cout << "Por favor, introduzca una pregunta o palabra clave:" << endl;
    cin >> palabra;


    for(int i = 0; i < set.size(); ++i){

        bool pbrake = str_search(set[i].pregunta, palabra, 0);
        if (pbrake == bool(true)){


            set[i].Definicion::mostrarInformacion();

            menu(i, set, true);

            
        }

    }

}



void menu(int index, vector <largaDefinicion> set1 , bool defl){



    int opcion;

    // Texto del menú que se verá cada vez
    cout << "\n\nMenu de Opciones" << endl;
    cout << "1. Mostrar todas las preguntas almacenadas." << endl;
    cout << "2. Hacer una pregunta" << endl;
    if (defl == true) {cout << "3. Mostrar definicion larga" << endl; }
    cout << "0. SALIR" << endl;
    
    cout << "\nIngrese una opcion: ";
    cin >> opcion;
    
    switch (opcion) {
        case 1:
            // Lista de instrucciones de la opción 1                
            
            // For para recorrer el arreglo de todas las preguntas
            for(int i = 0; i < set1.size(); ++i){

                cout << set1[i].pregunta << endl;


            }

            menu(0, set1);

            break;
            
        case 2:
            // Lista de instrucciones de la opción 2                
            

            vsearch(set1);

            break;

        
        case 3:

            if (defl == false){menu(0, set1);} 
            else{
            cout << "caso #siiiiiii" << endl;
            }
        case 0:
            return;
            break;
    } 

    


}
