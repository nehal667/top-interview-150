# Day 42 - Number of 1 Bits (Hamming Weight)
# LeetCode Problem

class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = bin(n)[2:]
        return bits.count("1")
