# LeetCode: Two Sum II - Input Array Is Sorted
# Difficulty: Medium
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# Use two pointers: left at start, right at end.
# If sum is too small, move left forward to increase sum.
# If sum is too large, move right backward to decrease sum.
# Return 1-indexed positions.

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum == target:
                return [l + 1, r + 1]
            elif curr_sum < target:
                l += 1
            else:
                r -= 1
