# Day 43 - Single Number
# LeetCode Problem

class Solution(object):
    def singleNumber(self, nums):
        # Initialize unique number
        uniqNum = 0

        # XOR all elements
        for num in nums:
            uniqNum ^= num

        return uniqNum
