# LeetCode: Longest Consecutive Sequence
# Difficulty: Medium
# Approach: HashSet (Start sequence only at smallest element)
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# Store all numbers in a set for O(1) lookup.
# Only start counting when the previous number (n-1) does not exist.
# Extend the sequence forward and track the maximum length.

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for n in num_set:
            if (n - 1) not in num_set:
                length = 1
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)

        return longest
