# Дан список неотрицательных целых чисел nums. Организуйте их таким образом, чтобы они составляли наибольшее число и верните его.
# Поскольку результат может быть очень большим, вам необходимо вернуть строку вместо целого числа.

"""
Input: nums = [10,2]
Output: "210"
"""

class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = "".join(sorted(map(str, nums), key=LargerNumKey))
        return "0" if largest_num[0] == "0" else largest_num
    

if __name__ == "__main__":
   largestNumber = Solution()
   result = Solution.largestNumber(largestNumber, [10,2])
   print(result)

