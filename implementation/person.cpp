#include "person.h"
#include <iostream>

Person::Person(const std::string& name, int age) : name(name), age(age) {}

void Person::introduce() const {
	std::cout << "Меня зовут" << name << "и мне " << age << " лет." << std::endl;
	
