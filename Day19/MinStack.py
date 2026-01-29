# LeetCode: Min Stack
# Difficulty: Medium
# Approach: Two Stacks
# Time Complexity: O(1) for all operations
# Space Complexity: O(n)
#
# Explanation:
# - stack stores all values
# - minStack stores the minimum value at each level
# - On push, store min(current value, previous min)
# - getMin() always returns the top of minStack

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(self.minStack[-1], val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
