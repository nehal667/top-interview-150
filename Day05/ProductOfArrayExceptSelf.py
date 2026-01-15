# LeetCode: Product of Array Except Self
# Difficulty: Medium
# Approach: Prefix (left) + Suffix (right) products
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# left[i]  = product of all elements before i
# right[i] = product of all elements after i
# result[i] = left[i] * right[i]

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1] * length
        right = [1] * length
        result = [1] * length

        # Build left products
        for i in range(1, length):
            left[i] = left[i - 1] * nums[i - 1]

        # Build right products
        for i in range(length - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # Multiply left and right for final answer
        for i in range(length):
            result[i] = left[i] * right[i]

        return result
