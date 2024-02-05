# Создание frozenset
frozen_set = frozenset([1, 2, 3, 4, 5])

# Вывод frozenset
print("Frozen Set: ", frozen_set)

# Попытка изменить frozenset выводит ошибку
# frozen_set.add(6) # AttributeError: 'frozenset' object has no attribute 'add'

# Операции, которые возвращают новый frozenset
union_set = frozen_set.union({5, 6, 7})
intersection_set = frozen_set.intersection({4, 5, 6})

print("Union Set: ", union_set)
print("Intersection Set: ", intersection_set)
