class DBconnect:
    """Реализация алгоритма Singleton"""
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f"Соединение с БД: {self.user}, {self.password}, {self.port}.")


db1 = DBconnect("Ruslan", 12345, 80)
db2 = DBconnect("Artur", 54321, 81)              
print(id(db1), id(db2))
