# Day 43 - Single Number (HashMap Approach)
# LeetCode Problem

from collections import defaultdict

class Solution:
    def singleNumber(self, nums):
        count = defaultdict(int)

        # Count frequency of each number
        for x in nums:
            count[x] += 1

        # Find element appearing once
        for x, freq in count.items():
            if freq == 1:
                return x

        return -1
