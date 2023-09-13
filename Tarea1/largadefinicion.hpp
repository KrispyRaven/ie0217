/**
 * @file function.hpp
 * @author Noel Blandon
 * @date 12/09/2023
 * @brief Definicion de clase Padre
*/
#ifndef LARGADEFINICION_H
#define LARGADEFINICION_H
#include "definicion.hpp"
#include <iostream>
#include <string>
#include <vector>

using namespace std;

/**
 * @brief clase largaDefinicion, hija de la clase padre. Agrega el parametro definicion larga
 * @param ldefinicion almacena la definicion larga
*/
class largaDefinicion : public Definicion {

    public:
    string ldefinicion;

    largaDefinicion(int n, string preg, string def_c, string def_l) : Definicion(n , preg, def_c) , ldefinicion(def_l){}

    /**
     * @brief Metodo que devuelve una impresion de la definicion larga
    */
    void mostrarInformacion();

};


#endif