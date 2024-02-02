def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) //2      # Находим середину массива
        left_half = arr[:mid]   # Делим массив на две части
        right_half = arr[mid:]

        merge_sort(left_half)   # Рекурсивно сортируем левую часть
        merge_sort(right_half)  # Рекурсивно сортируем правую часть
        
        merge(arr, left_half, right_half)   # Сливаем отсортиованные части

def merge(arr, left, right):
    i = j = k = 0   # Индексы для перебора left, right и основного массива arr

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        j += 1
        k += 1

# Пример использования
array = [38, 27, 43, 3, 9, 82, 10]
merge_sort(array)
print("Отсортированный массив: ", array)
