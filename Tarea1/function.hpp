/**
 * @file function.hpp
 * @author Noel Blandon
 * @date 12/09/2023
 * @brief Funciones de utilidad
*/
#ifndef FUNCTION_H
#define FUNCTION_H
#include <iostream>
#include <string>
#include <vector>
#include "largadefinicion.hpp"
using namespace std;


/**
 * @brief menu ejecuta el menu principal
 * @param index indica el indice de al que se desea posicionar el vector para ejecutar la demostracion de la demostracion larga
 * @param set1 Es el set de vectores de la clase de definiciones
 * @param defl Nos indica si hay que mostrar el boton de definicion larga
*/
void menu(int index, vector <largaDefinicion> set1 , bool defl = false);

/**
 * @brief vsearch realiza la busqueda de una palabra clave solicitada al usuario. Ademas itera la funcion de de busqueda dentro del arreglo de vectores
 * @param set Es el set de vectores de la clase de definiciones
*/
void vsearch(vector <largaDefinicion> set );

/**
 * @brief str_search hace la busqueda mediante comparacion de la palabra a buscar en un string.
 * @param strsearch parrafo en el cual se debe buscar
 * @param strlocation palabra a buscar 
 * @param k indice de comparacion
*/
bool str_search(string strsearch, string strlocation, int k);



//si
#endif