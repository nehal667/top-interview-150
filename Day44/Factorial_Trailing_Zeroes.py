# Day 44 - Factorial Trailing Zeroes
# LeetCode Problem

class Solution(object):
    def trailingZeroes(self, n):
        count = 0
        divisor = 5

        # Count multiples of 5, 25, 125...
        while n >= divisor:
            count += n // divisor
            divisor *= 5

        return count
