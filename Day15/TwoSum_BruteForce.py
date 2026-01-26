# LeetCode: Two Sum
# Difficulty: Easy
# Approach: Brute Force (Two Loops)
# Time Complexity: O(n^2)
# Space Complexity: O(1)
#
# Explanation:
# Check every pair (i, j). If nums[i] + nums[j] == target, return [i, j].

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []
