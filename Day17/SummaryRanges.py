# LeetCode: Summary Ranges
# Difficulty: Easy
# Approach: Single pass / Range tracking
# Time Complexity: O(n)
# Space Complexity: O(1) (excluding output list)
#
# Explanation:
# Traverse the sorted array and group consecutive numbers.
# If a range has one number, store "a".
# If it has multiple numbers, store "a->b".

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []

        if not nums:
            return result

        start = nums[0]

        for i in range(1, len(nums) + 1):
            # If end of array OR numbers are not consecutive
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(nums[i - 1]))

                if i < len(nums):
                    start = nums[i]

        return result
