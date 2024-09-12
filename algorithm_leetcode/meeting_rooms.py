# Дан массив интервалов времени встреч, где intervals[i] = [starti, endi]. Определите, может ли человек посетить все встречи.

"""
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
"""

from typing import List

class Solution:
    def canAttendmeeting(self, intervals: List[List[int]]) -> bool:
        def overlap(interval1: List[int], interval2: List[int]) -> bool:
            return (interval1[0] >= interval2[0] and interval1[0] <= interval2[1] or interval2[0] >= interval1[0] and interval2[0] <interval1[1])

        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if overlap(intervals[i], intervals[j]):
                    return False
        return True
    
if __name__ == "__main__":
   example = Solution()
   result = Solution.canAttendmeeting(example, intervals = [[0,30],[5,10],[15,20]])
   print(result)