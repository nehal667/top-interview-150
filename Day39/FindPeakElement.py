# LeetCode: Find Peak Element
# Difficulty: Medium
#
# Approach:
# Binary Search
# A peak element is greater than its neighbors.
# If nums[mid] > nums[mid+1], peak lies on left side.
# Otherwise, peak lies on right side.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left
