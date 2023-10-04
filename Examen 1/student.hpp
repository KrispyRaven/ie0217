#ifndef STUDENT_H
#define STUDENT_H

#include <iostream>
#include <string>

using namespace std;

/* Creacion de la clase Estudiante */
class Estudiante {
private:

    /* Definicion de atributos */

    string nombre;

    float* calificacion;

public:

    /* Constructor de la clase */
    Estudiante(const string& _nombre, float _calificacion);

    /* Destructor de la clase*/
    ~Estudiante();

    /* Metodos de la clase */
    void MostrarInformacion();
};

#endif