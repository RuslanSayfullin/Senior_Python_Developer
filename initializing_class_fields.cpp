#include <iostream>

class MyClass {
public:
	int value;

	// Конструктор с параиетром дляя инициализации поля value
	MyClass(int val) : value(val) {}
};

int main() {
	MyClass obj(42);	// Создание обьекта с инициализацией поля value значением 42
	return 0;
}
