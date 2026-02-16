# LeetCode: Generate Parentheses
# Difficulty: Medium
# Approach: Backtracking
#
# Idea:
# - Add '(' if we still have opening brackets left.
# - Add ')' only if it won’t break validity (close < open).
# - Stop when length reaches 2 * n.
#
# Time Complexity:
#   O(4^n / sqrt(n))  (Catalan numbers)
# Space Complexity:
#   O(n) recursion stack

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openP: int, closeP: int, s: str) -> None:
            # If the string length is complete
            if openP == closeP and openP + closeP == 2 * n:
                res.append(s)
                return
            
            # Add opening parenthesis if possible
            if openP < n:
                dfs(openP + 1, closeP, s + "(")
            
            # Add closing parenthesis only if valid
            if closeP < openP:
                dfs(openP, closeP + 1, s + ")")

        dfs(0, 0, "")
        return res
