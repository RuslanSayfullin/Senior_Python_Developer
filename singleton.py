class DBconnect:
    """Реализация алгоритма Singleton"""
    def __new__(cls, *args, **kwargs):
        print("Вызов __new__")

    def __init__(self, x, y):
        self.x = x
        self.y = y


db = DBconnect(1, 2)
print(db)
