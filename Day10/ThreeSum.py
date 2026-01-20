# LeetCode: 3Sum
# Difficulty: Medium
# Approach: Sort + Two Pointers
# Time Complexity: O(n^2)
# Space Complexity: O(1) extra (excluding output)
#
# Explanation:
# Sort the array. Fix one number nums[i], then use two pointers (j, k)
# to find pairs such that nums[i] + nums[j] + nums[k] == 0.
# Skip duplicates for i and j to avoid repeated triplets.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        nums.sort()

        for i in range(len(nums)):
            # Skip duplicate fixed elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                tot = nums[i] + nums[j] + nums[k]

                if tot > 0:
                    k -= 1
                elif tot < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1

                    # Skip duplicates for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return result
