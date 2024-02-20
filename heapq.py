import heapq

# Создаём список
list = [5, 3, 17, 2, 8, 4]

# Приобразуем список в кучу
heapq.heapify(list)

# Минимальный элемент
min_element = list[0]

# Добавляем элемент
heapq.heappush(list, 1)

# Извлекаем минимальные элемент
min_element = heapq.heappop(list)

print(list)
