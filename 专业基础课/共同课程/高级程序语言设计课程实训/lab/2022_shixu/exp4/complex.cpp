#include <iostream>
#include <cmath>
#include <string>
#include "my_complex.h"
using namespace std;

complex::complex() {
    real = 0;
    imag = 0;
}

complex::~complex() {}

complex::complex(double r, double i) {
    real = r;
    imag = i;
}

ostream& operator<<(ostream& os, const complex& c) {
    if (c.imag < 0)
        os << c.real << "-" << c.imag << "i";
    else
        os << c.real << "+" << c.imag << "i";
    return os;
}

istream& operator>>(istream& is, complex& c) {
    char sign, ch;
    if (is >> c.real) {
        sign = getchar();
        if (sign == '\n') {
            c.imag = 0;
            return is;
        }
        if (sign == '+') {
            if (is >> c.imag >> ch) {
                if (ch == 'i') {
                    return is;
                }
                cout << "error" << endl;
                is.setstate(ios::failbit);
            }
        }
        else if (sign == '-') {
            if (is >> c.imag >> ch) {
                if (ch == 'i') {
                    c.imag = -c.imag;
                    return is;
                }
                cout << "error" << endl;
                is.setstate(ios::failbit);
            }
        }
        else if (sign == 'i') {
            c.imag = c.real;
            c.real = 0;
        }
        else if (sign == ' ') {
            sign = getchar();
            if (sign == '+') {
                if (is >> c.imag >> ch) {
                    if (ch == 'i') {
                        return is;
                    }
                    cout << "error" << endl;
                    is.setstate(ios::failbit);
                }
            }
            else if (sign == '-') {
                if (is >> c.imag >> ch) {
                    if (ch == 'i') {
                        c.imag = -c.imag;
                        return is;
                    }
                    cout << "error" << endl;
                    is.setstate(ios::failbit);
                }
            }
            else {
                cout << "error" << endl;
                is.setstate(ios::failbit);
            }
        }
        else {
            cout << "error" << endl;
            is.setstate(ios::failbit);
        }
    }
    else {
        cout << "error" << endl;
        is.setstate(ios::failbit);
    }
    return is;
}
