# Day 44 - Plus One
# LeetCode Problem

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        # Traverse digits from end
        for i in range(len(digits) - 1, -1, -1):
            s = digits[i] + carry
            digits[i] = s % 10
            carry = s // 10

        # If carry remains, add new digit
        if carry:
            digits = [1] + digits

        return digits
