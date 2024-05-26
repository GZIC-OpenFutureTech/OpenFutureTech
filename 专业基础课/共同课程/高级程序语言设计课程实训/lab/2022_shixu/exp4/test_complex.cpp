#include <iostream>
#include <cmath>
#include <string>
#include "my_complex.h"
using namespace std;

int main() {
	cout << "Test Complex" << endl;
    cout << "input format: a+bi or a + bi or a +bi or a+ bi" << endl;
    complex complex_1;
    cin >> complex_1;
    cout << complex_1 << endl;
    return 0;

}