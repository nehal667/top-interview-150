# LeetCode: Maximum Subarray
# Difficulty: Medium
# Approach: Kadane's Algorithm
#
# Idea:
# - Keep a running sum of the subarray.
# - If the running sum becomes negative, reset it.
# - Track the maximum sum seen so far.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currentSum = 0
        
        for num in nums:
            currentSum += num
            maxSum = max(maxSum, currentSum)
            
            if currentSum < 0:
                currentSum = 0
        
        return maxSum
