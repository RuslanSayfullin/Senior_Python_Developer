from collections import Counter

# Создаём Counter из списка
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(my_list)

# Выводим результат подчёта
print(counter)

# Получаем количество вхождения конкретного элемента
print(counter['banana'])

# Метод elements() возвращает итератор по всем элементам с учётом их количества
print(list(counter.elements()))

# наиболее часто встречающиеся в элементы
print(counter.most_common(2))
