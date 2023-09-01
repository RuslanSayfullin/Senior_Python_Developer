class A:
    def do_something(sef):
        print("A's method")

class B(A):
    def do_something(self):
        print("B's method")

class C(A):
    def do_something(self):
        print("C's method")

class D(B, C):
    pass

d = D()
d.do_something()    # Выводит "B's method"
print(D.__mro__)    # Выводит порядок разрешения методов
