#include<iostream>
using namespace std;

class Employee{
    private:
    int val;
    string name;

    Employee(int val, string name){
        this->val = val;
        this->name = name;
    }

    public: string PrintName(){
        return this->name;
    }
};

int main()
{
    // Employee emp1 = Employee(1, "Gourav kumar singh");
    emp1.PrintName();
}

