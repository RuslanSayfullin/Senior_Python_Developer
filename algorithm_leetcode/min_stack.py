# Разработайте стек, который поддерживает операции добавления элемента, удаления элемента, 
# получения верхнего элемента и извлечения минимального элемента за постоянное время.
# реализовать решение с временной сложностью O(1) для каждой функции.

"""
Пример:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x:int) -> None:
        if not self.stack:
            self.stack.append((x, x))
            return
        current_min = self.stack[-1][1]
        self.stack.append((x, min(x, current_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
    
    def getMin(self) -> int:
        return self.stack[-1][1]
    
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()
    minStack.pop()
    minStack.top()
    minStack.getMin()