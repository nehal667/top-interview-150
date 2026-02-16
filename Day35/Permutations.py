# LeetCode: Permutations
# Difficulty: Medium
# Approach: Backtracking (In-place swapping)
#
# Idea:
# - Fix one position at a time.
# - Swap the current element with every possible element ahead.
# - Backtrack by undoing the swap.
#
# Time Complexity:
#   O(n! * n)
# Space Complexity:
#   O(n) for recursion stack

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i: int) -> None:
            # If all positions are fixed, add permutation
            if i == len(nums):
                res.append(nums[:])
                return
            
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]   # choose
                backtrack(i + 1)                      # explore
                nums[i], nums[j] = nums[j], nums[i]   # un-choose (backtrack)

        backtrack(0)
        return res
