def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо")
    return x / y

# Пример использования
try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Ошибка: {e}")
else:
    print(f"Результат: {result}")
