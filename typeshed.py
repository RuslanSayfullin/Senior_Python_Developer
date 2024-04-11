from typing import List

def my_function(numbers: List[int]) -> int:
    """
    Суммирует список чисел.
    """

    total = 0
    for number in numbers:
        total += number

    return total

if __name__ == "__main__":
    result = my_function([1, 2, 3, 4, 5])
    print(result)
