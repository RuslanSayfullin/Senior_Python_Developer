# Даны головы двух односвязных списков headA и headB. Верните узел, в котором эти два списка пересекаются. 
# Если два связанных списка не имеют пересечений, верните null.

"""
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. 
In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.
"""

class ListNode:
  def __init__(self,val=0,next=None):
    self.val = val
    self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        while headA is not None:
            pB = headB
            while pB is not None:
                if headA == pB:
                    return headA
                pB = pB.next
            headA = headA.next
        
        return None
    
if __name__ == "__main__":
   minStack = Solution()
   Solution.getIntersectionNode(minStack, [4,1,8,4,5], [5,6,1,8,4,5])

