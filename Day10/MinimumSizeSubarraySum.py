# LeetCode: Minimum Size Subarray Sum
# Difficulty: Medium
# Approach: Sliding Window (Two Pointers)
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# Since all numbers are positive, we can use a sliding window.
# Expand the window by moving right and adding nums[right] to curr_sum.
# When curr_sum >= target, shrink from the left to minimize the window length.

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        ans = float("inf")

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                ans = min(ans, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if ans == float("inf") else ans
