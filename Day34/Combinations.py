# LeetCode: Combinations
# Difficulty: Medium
# Approach: Backtracking
#
# Idea:
# - Generate all possible combinations of k numbers from 1 to n.
# - Use backtracking to build combinations incrementally.
#
# Time Complexity:
#   O(C(n, k))
# Space Complexity:
#   O(k) for recursion stack

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(start: int) -> None:
            # If combination size reaches k, add to result
            if len(comb) == k:
                res.append(comb[:])
                return
            
            # Try numbers from 'start' to 'n'
            for num in range(start, n + 1):
                comb.append(num)
                backtrack(num + 1)
                comb.pop()  # Backtrack

        backtrack(1)
        return res
