# Разработайте структуру данных, которая принимает поток целых чисел и проверяет,
# есть ли в ней пара чисел, сумма которых равна определенному значению.

"""
Input
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output
[null, null, null, null, true, false]
"""

class TwoSum(object):

    def __init__(self) -> None:   
        self.nums = []
        self.is_sorted = False

    def add(self, number: int) -> None:
        self.nums.append(number)
        self.is_sorted = False

    def find(self, value: int) -> bool:
        if not self.is_sorted:
            self.nums.sort()
            self.is_sorted = True

        low, high = 0, len(self.nums) - 1
        while low < high:
            currSum = self.nums[low] + self.nums[high]
            if currSum < value:
                low += 1
            elif currSum > value:
                high -= 1
            else: return True

        return False
    
if __name__ == "__main__":
    instance = TwoSum()
