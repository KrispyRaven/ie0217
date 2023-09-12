#ifndef FUNCTION_H
#define FUNCTION_H
#include <iostream>
#include <string>
#include <vector>
#include "largadefinicion.hpp"
using namespace std;



void menu(int index, vector <largaDefinicion> set1 , bool defl = false);

void vsearch(vector <largaDefinicion> set );

bool str_search(string strsearch, string strlocation, int k);



//si
#endif