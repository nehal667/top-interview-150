# LeetCode: Majority Element
# Difficulty: Easy
# Approach: Hash Map (Frequency Count)
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# Count the frequency of each element using a dictionary.
# The element with the maximum frequency is the majority element.

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        return max(freq, key=freq.get)
