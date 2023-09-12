
#include "function.hpp"
#include <iostream>
#include <string>
#include <vector>

using namespace std;

largaDefinicion q1(1,"pregunta","definicion cortas","definicion larguisima");
largaDefinicion q2(2,"pregunta2","definicion corta2","definicion larguisima2");
largaDefinicion q3(3,"pregunta3","definicion corta3","definicion larguisima3");

vector <largaDefinicion> set1 = {q1,q2,q3};


int main() {

    menu(0, set1 ,false);
     
    return 0;

}

