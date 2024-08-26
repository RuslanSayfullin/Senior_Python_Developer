# Дан массив целых чисел nums. Верните максимальную разницу между двумя последовательными элементами в его отсортированной форме. 
# Если массив содержит менее двух элементов, верните 0.

"""
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
"""

class Solution:
    def maximumGap(self, nums):
        if (nums is None or len(nums) < 2):
            return 0
        
        nums.sort()
        maxGap = 0

        for i in range(len(nums) - 1):
            maxGap = max(nums[i + 1] - nums[i], maxGap)

        return maxGap
    
if __name__ == "__main__":
    instance = Solution()
    print(instance.maximumGap(nums = [3,6,9,1]))  # Результат будет напечатан в консоль
