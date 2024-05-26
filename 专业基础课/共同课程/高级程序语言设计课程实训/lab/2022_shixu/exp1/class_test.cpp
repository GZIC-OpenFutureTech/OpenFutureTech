#include <iostream>
#include "student.h"
#include "manager.h"
#include <string>

void ModifyStudent(Student& student1, double newscore) {
    student1.score = newscore;
}

int main() {
    Student::totalStudents = 0;
    Student student1("Alice", 1, 95.5);
    Student student2("Bob", 2, 88.0);

    student1.Print();
    student2.Print();

    ModifyStudent(student1, 98.5);
    student1.Print();

    Student student3 = student1; // Copy constructor
    student3.Print();

    student2 = student1; // Assignment operator overloading
    student2.Print();

    double score = student1; // User-defined conversion
    std::cout << "Student 1's score as a double: " << score << std::endl;

    Manager::ModifyAnyStudent(student1, "Charlie", 3, 92.0);
    student1.Print();

    Manager manager;
    manager.PrintTotalStudents();

    return 0;
}

