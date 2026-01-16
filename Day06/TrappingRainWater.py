# LeetCode: Trapping Rain Water
# Difficulty: Hard
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# Use two pointers (left, right) and track the maximum height seen so far from both sides
# (left_max, right_max). Water trapped at a position depends on the smaller of the two maxima.
# Move the pointer with the smaller max inward and add trapped water.

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        curr_water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                curr_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                curr_water += right_max - height[right]

        return curr_water
