#pragma once
#ifndef MANAGER_H
#define MANAGER_H
#include <string>

class Student; // Forward declaration

class Manager {
public:
    static void ModifyAnyStudent(Student& student, const std::string& newName, int newID, double newScore);
    void PrintTotalStudents();
};

#endif