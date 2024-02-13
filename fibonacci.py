from functools import lru_cache

@lru_cache(maxsize=100)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Вычисление первых 10 чисел Фибоначчи
for i in range(10):
    print(fibonacci(i))


