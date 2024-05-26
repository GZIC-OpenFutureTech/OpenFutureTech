#pragma once
#ifndef STUDENT_H
#define STUDENT_H
#include <string>

class Student {


    friend void ModifyStudent(Student& student, double newScore);
    friend class Manager;

private:
    std::string name;
    int studentID;


    double score;

public:
    static int totalStudents;

    Student(const std::string& n, int id, double s);
    ~Student();
    Student(const Student& other);
    void Print() const;


    void ModifyScore(double newScore);
    Student& operator=(const Student& other);
    double GetScore() const;


    operator double() const;
};

#endif