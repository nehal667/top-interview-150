# LeetCode: Remove Duplicates from Sorted Array II
# Difficulty: Medium
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# Since the array is sorted, duplicates are adjacent.
# We allow at most two occurrences by checking nums[k-2].
# If the current element is different, we place it at index k.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        k = 2  # first two elements are always allowed

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k
