#include <iostream>

class Base {
public:
	int value;
};

class Derived1 : virtual public Base {
};

class Derived2 : virtual public Base {
};

class FinalDerived : public Derived1, public Derived2 {
};

int main() {
	FinalDerived obj;
	obj.value = 42;	// Это безопасно, так как value находитя в общем базовом классе
	return 0;
}
