# LeetCode: Rotate Array
# Difficulty: Medium
# Approach: Reverse Array (In-place)
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# Rotating the array to the right by k steps can be done by:
# 1. Reversing the entire array
# 2. Reversing the first k elements
# 3. Reversing the remaining elements

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        # Helper function to reverse part of the array
        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Step 1: Reverse entire array
        reverse(0, n - 1)
        # Step 2: Reverse first k elements
        reverse(0, k - 1)
        # Step 3: Reverse remaining elements
        reverse(k, n - 1)
