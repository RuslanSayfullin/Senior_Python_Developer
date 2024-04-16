class Singleton:
    _isinstance = None

    def __new__(cls):
        if cls._isinstance == None:
            cls._isinstance = super().__new__(cls)

        return cls._isinstance

a = Singleton()
b = Singleton()

print(a is b)
