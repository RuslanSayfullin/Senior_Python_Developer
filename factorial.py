def factorial(n):
    """
    Вычисляем факториал числа n.
    """

    if n < 0:
        raise ValueError("n должно быть неотрицательным")

    if n == 0:
        return 1

    return n * factorial(n-1)

def main():
    print(factorial(5))

if __name__ == "__main__":
    main()
