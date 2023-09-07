#include "student.hpp"
#include "function.hpp"
#include <iostream>

using namespace std;



int main() {

    Student student1(88.0), student2(56.0);

    calculateAverage(student1, student2);

    cout << "end" << endl;

return 0;

}