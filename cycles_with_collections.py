# исходный списокчисел
lst = list(range(10))
print(lst)

squares = []
# цикл для коллекции
for i in lst:
           squares.append(i * i)
print(squares)

squares = [num * num for num in lst]
print(squares)

squares = list(map(lambda x: x * x, lst))
print(squares)

