# LeetCode: Evaluate Reverse Polish Notation
# Difficulty: Medium
# Approach: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# - Traverse tokens left to right
# - If token is a number → push to stack
# - If token is an operator → pop last two numbers, apply operation, push result
# - Division truncates toward zero → use int(a / b)

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # division
                    stack.append(int(a / b))  # truncate toward zero

        return stack[0]
