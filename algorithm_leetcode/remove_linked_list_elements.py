# Для заданного начала связного списка и целого числа val удалите все узлы связного списка, у которых Node.val равно val, и верните новое начало списка.

"""
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        
        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return sentinel.next
    
if __name__ == "__main__":
   removeElements = Solution()
   result = Solution.removeElements(removeElements,head = [1,2,6,3,4,5,6], val = 6)
   print(result)