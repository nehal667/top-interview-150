# LeetCode: Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
#
# Approach:
# Binary Search twice:
# 1. Find first occurrence
# 2. Find last occurrence
#
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]

        # Find starting index
        ans[0] = self.binarySearch(nums, target, True)

        # Find ending index only if start exists
        if ans[0] != -1:
            ans[1] = self.binarySearch(nums, target, False)

        return ans

    def binarySearch(self, nums, target, findStartIndex):
        ans = -1
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                ans = mid
                if findStartIndex:
                    end = mid - 1   # Move left
                else:
                    start = mid + 1 # Move right

        return ans
