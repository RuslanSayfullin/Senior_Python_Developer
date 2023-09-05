class MyClass:
    class_variable = 10

    def __init__(self, value):
        self.value = value

    @classmethod
    def class_method(cls):
        print("This is a class method")
        print(f"Class variable: {cls.class_variable}")

    def instance_method(self):
        print("This is an instance method")
        print(f"Instance variable: {self.value}")

# Создаем экземпляр класса
obj = MyClass(20)

# Вызываем классовый метод
MyClass.class_method()

# Вызываем метод экземпляра
obj.instance_method()
