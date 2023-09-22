#include <utility>

int main() {
	int a = 3, b = 5;

	// Меняем a и b местами с помощью std::swap
	std::swap(a, b);

	// Теперь a = 5, b = 3
	std::string s1 = "Hello", s2 = "World";

	// Меняем строки s1 и s2 местами
	std::swap(s1 , s2);

	// Теперь s1 содержит "World", а s2 содержит "Hello"
	std::vector<int> v1{1, 2, 3}, v2{4, 5};

	// Меняем векторы v1 и v2 местами
	std::swap(v1, v2);

	// Теперь v1 сожержит {4, 5}, а v2 содержит {1, 2, 3}
	return 0;
}
