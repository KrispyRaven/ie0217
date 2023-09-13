/**
 * @file function.hpp
 * @author Noel Blandon
 * @date 12/09/2023
 * @brief Definicion de clase Padre
*/

#ifndef DEFINICION_H
#define DEFINICION_H
#include <iostream>
#include <string>
#include <vector>

using namespace std;


/**
 * @brief clase Definicion es la padre de todas las clases, se encarga de almacenar la pregunta y definicion
 * @param pregunta almacena la pregunta
 * @param definicion almacena la definicion corta 
*/
class Definicion {

    public:
    int pos_number;
    string pregunta;
    string definicion;

    /**
     * @brief Constructor de la clase Definicion 
    */
    Definicion(int n, string preg, string def_c) : pos_number(n), pregunta(preg), definicion(def_c){}

    /**
     * @brief Metodo que devuelve una impresion de la definicion corta
    */
    void mostrarInformacion();

};

#endif