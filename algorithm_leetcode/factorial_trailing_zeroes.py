# Дано целое число n, верните количество конечных нулей в n!
# Обратите внимание, что n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

"""
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:

        n_factorial = 1
        for i in range(2, n + 1):
            n_factorial *= i

        zero_count = 0
        while n_factorial % 10 == 0:
            zero_count += 1
            n_factorial //= 10

        return zero_count
    
if __name__ == "__main__":
    instance = Solution()
    print(instance.trailingZeroes(n = 3))  # Результат будет напечатан в консоль
