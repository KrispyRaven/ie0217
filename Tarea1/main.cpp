
#include "function.hpp"
#include <iostream>
#include <string>
#include <vector>

using namespace std;





class Definicion {

    public:
    int pos_number;
    string pregunta;
    string definicion;

    Definicion(int n, string preg, string def_c) : pos_number(n), pregunta(preg), definicion(def_c){}

    void mostrarInformacion() {

        cout << definicion << endl;
    }

};

class largaDefinicion : public Definicion {

    public:
    string ldefinicion;

    largaDefinicion(int n, string preg, string def_c, string def_l) : Definicion(n , preg, def_c) , ldefinicion(def_l){}

    void mostrarInformacion() {

        cout << ldefinicion << endl;
    }

};


largaDefinicion q1(1,"pregunta","definicion cortas","definicion larguisima");
largaDefinicion q2(2,"pregunta1","definicion corta2","definicion larguisima2");
largaDefinicion q3(3,"pregunta3","definicion corta3","definicion larguisima3");

vector <largaDefinicion> set1 = {q1,q2,q3};

int main() {





int opcion;
    bool repetir = true;
    
    do {

        string parrafo = "Respuesta corta: Un arreglo en C++ es una estructura de datos de tamaño fijo que almacena elementos en ubicaciones de memoria contiguas, mientras que una lista (como std::list o std::vector) es una estructura de datos dinámica de tamaño variable que almacena elementos en ubicaciones de memoria no necesariamente contiguas. Respuesta intermedia: La diferencia clave entre un arreglo y una lista en C++ radica en su tamaño y ubicación de memoria. Un arreglo tiene un tamaño fijo en tiempo de compilación y almacena elementos en ubicaciones de memoria contiguas, lo que permite un acceso rápido y constante a los elementos. En contraste, una lista puede cambiar de tamaño durante la ejecución y almacena elementos en ubicaciones de memoria dispersas, lo que facilita la inserción y eliminación eficiente de elementos, pero puede tener un acceso más lento a elementos específicos.";

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
                
                for(int i = 0; i < set1.size(); ++i){

                    cout << set1[i].pregunta << endl;

                }

                // Hacer la integracion del menu interno de imprecion de las preguntas 

                break;
                
            case 2:
                // Lista de instrucciones de la opción 2                
                
                cout << "caso #2" << parrafo.length() << endl;
                break;

            
            case 0:
            	repetir = false;
            	break;
        }        
    } while (repetir);
	 
    return 0;

}