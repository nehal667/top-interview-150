# LeetCode: Merge Sorted Array
# Difficulty: Easy
# Approach: Replace empty slots and sort
# Time Complexity: O((m + n) log(m + n))
# Space Complexity: O(1)
# Note: Simple approach; optimal solution uses two pointers.

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()
