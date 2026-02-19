# LeetCode: Search Insert Position
# Difficulty: Easy
#
# Problem:
# Given a sorted array and a target value,
# return the index if the target is found.
# If not, return the index where it should be inserted.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # If target exists, return its index
        if target in nums:
            return nums.index(target)

        # If target smaller than first element
        if target < nums[0]:
            return 0

        # If target greater than last element
        if target > nums[-1]:
            return len(nums)

        # Find correct insert position
        for i in range(len(nums)):
            if nums[i] > target:
                return i
