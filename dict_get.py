my_dict = {'a': 1, 'b': 2, 'c': 3}

# Используем get() для получения значения по ключу 'b'
value_b = my_dict.get('b')
print(value_b)  # Вывод: 2

# Используем get() для получения значения по ключу 'd' (ключа, которого нет в словаре)
value_d = my_dict.get('d')
print(value_d)  # Вывод: None

# Используем get() с заданным значением по умолчанию
value_e = my_dict.get('e', 0)
print(value_e)  # Вывод: 0
