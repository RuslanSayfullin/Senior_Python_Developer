import functools

@functools.lru_cache(maxsize=None)
def factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial(m-1, n*acc)

result = factorial(5)
print(result)   # Выведет: 120
