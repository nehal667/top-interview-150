# LeetCode: Maximum Sum Circular Subarray
# Difficulty: Medium
# Approach: Kadane’s Algorithm (Max + Min Subarray)
#
# Idea:
# 1. Find normal maximum subarray sum using Kadane's algorithm.
# 2. Find minimum subarray sum.
# 3. Circular maximum = total_sum - minimum_subarray_sum.
# 4. Handle edge case when all numbers are negative.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_min = curr_max = min_sum = max_sum = total_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Maximum subarray (Kadane)
            curr_max = max(nums[i], curr_max + nums[i])
            max_sum = max(max_sum, curr_max)

            # Minimum subarray
            curr_min = min(nums[i], curr_min + nums[i])
            min_sum = min(min_sum, curr_min)

            total_sum += nums[i]

        # Edge case: all numbers negative
        if min_sum == total_sum:
            return max_sum

        # Maximum of normal or circular case
        return max(max_sum, total_sum - min_sum)
