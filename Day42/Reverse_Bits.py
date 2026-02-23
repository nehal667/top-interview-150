# Day 42 - Reverse Bits
# LeetCode Problem

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        # Reverse 32 bits
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1

        return res
