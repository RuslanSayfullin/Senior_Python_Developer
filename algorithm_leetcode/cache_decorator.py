from functools import wraps

def cache(func):
    cache_data = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache_data:
            print("Возвращаем кэшированный результат")
            return cache_data[args]
        result = func(*args)
        cache_data[args] = result
        return result
    return wrapper

@cache
def compute_square(n):
    print(f"Вычесляем квадрат для {n}")
    return n * n

# Пример использования
print(compute_square(4))
print(compute_square(4))