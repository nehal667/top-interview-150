# LeetCode: Valid Parentheses
# Difficulty: Easy
# Approach: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# Use a stack to store opening brackets.
# When a closing bracket appears, pop from the stack and check if it matches.
# If stack is empty at the end, the string is valid.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if bracket in {"(", "{", "["}:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if (bracket == ")" and popped != "(") or \
                   (bracket == "]" and popped != "[") or \
                   (bracket == "}" and popped != "{"):
                    return False

        return len(stack) == 0
