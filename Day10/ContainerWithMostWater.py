# LeetCode: Container With Most Water
# Difficulty: Medium
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# Start with two pointers at both ends. Compute area using width (r-l) and
# the smaller height. Move the pointer with the smaller height inward to
# possibly find a taller line and increase area.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res
