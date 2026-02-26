# Day 43 - Bitwise AND of Numbers Range
# LeetCode Problem

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Remove rightmost set bits until both numbers match
        while right > left:
            right &= right - 1

        return right
