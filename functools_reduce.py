from functools import reduce

# Вычисление суммы всех элементов списка при помощи reduce:
items = [10, 20, 30, 40, 50]
sum_all = reduce(lambda x, y: x + y, items)
print(sum_all)

# Вычисление наиюольшего элемента в списке при помощи reduce:
items = [1, 24, 17, 14, 9, 32, 2]
all_max = reduce(lambda a, b: a if(a > b) else b, items)
print(all_max)
