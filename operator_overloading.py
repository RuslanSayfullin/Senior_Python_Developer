class Thing:
    def __init__(self, value):
        self.__value = value

    # Переопределяем оператор >
    def __gt__(self, other):
        return self.__value > other.__value

    # Переопределяем оператор <
    def __lt__(self, other):
        return self.__value < other.__value

something = Thing(100)
nothing = Thing(0)

# True 
print(something > nothing)

# False
print(something < nothing)

# Error
print(something + nothing)
