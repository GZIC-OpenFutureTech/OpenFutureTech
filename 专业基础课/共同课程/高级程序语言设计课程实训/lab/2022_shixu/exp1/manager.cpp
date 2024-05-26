#include "manager.h"
#include "student.h"
#include <iostream>
#include <string>

void Manager::ModifyAnyStudent(Student& student, const std::string& newName, int newID, double newScore) {
    student.name = newName;
    student.studentID = newID;
    student.score = newScore;
}

void Manager::PrintTotalStudents() {
    std::cout << "Number of Students is " << Student::totalStudents << std::endl;
}
