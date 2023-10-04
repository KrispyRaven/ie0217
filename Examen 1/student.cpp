#include <iostream>
#include <string>
#include "student.hpp"


using namespace std;


Estudiante::Estudiante(const string& _nombre, float _calificacion) : nombre(_nombre) {
        
        /*Manejo de excepciones*/
        if (_calificacion < 0 || _calificacion > 100) {
            throw invalid_argument("La calificación debe estar entre 0 y 100.");
        }
        /* Asignacion en memoria dinamica*/
        calificacion = new float(_calificacion);
    }


Estudiante::~Estudiante() {
        delete calificacion;
    }

void Estudiante::MostrarInformacion(){

    cout << "Nombre del estudiante: " << nombre << std::endl;
    cout << "Calificación: " << *calificacion << std::endl;

}