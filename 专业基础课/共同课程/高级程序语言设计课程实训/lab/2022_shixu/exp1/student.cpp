#include "student.h"
#include <iostream>
#include <string>

int Student::totalStudents = 0;

Student::Student(const std::string& n, int id, double s) : name(n), studentID(id), score(s) {
    std::cout << "Student " << name << " has been created." << std::endl;
    totalStudents++;
}

Student::~Student() {
    std::cout << "Student " << name << " has been destroyed." << std::endl;
    totalStudents--;
}

Student::Student(const Student& other) : name(other.name), studentID(other.studentID), score(other.score) {
    std::cout << "Student " << name << " has been copied." << std::endl;
}

void Student::Print() const {
    std::cout << "Name: " << name << ", Student ID: " << studentID << ", Score: " << score << std::endl;
}

void Student::ModifyScore(double newScore) {
    score = newScore;
}

Student& Student::operator=(const Student& other) {
    if (this != &other) {
        name = other.name;
        studentID = other.studentID;
        score = other.score;
    }
    return *this;
}

double Student::GetScore() const {
    return score;
}

Student::operator double() const {
    return score;
}
