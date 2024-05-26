#include <iostream>
#include <cmath>
using namespace std;

class complex
{
private:
    double real;
    double imag;
public:
    complex();
    complex(double r, double i);
    ~complex();
    friend ostream& operator<<(ostream& os, const complex& c);
    friend istream& operator>>(istream& is, complex& c);
};

