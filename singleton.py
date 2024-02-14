class DBconnect:
    """Реализация алгоритма Singleton"""
    def __new__(cls, *args, **kwargs):
        print("Вызов __new__")
        return super().__new__(cls)

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f"Соединение с БД: {self.user}, {self.password}, {self.port}.")


db1 = DBconnect("Ruslan", 12345, 80)
db2 = DBconnect("Artur", 54321, 81)              
print(id(db1), id(db2))
