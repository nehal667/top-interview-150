# LeetCode: Integer to Roman
# Difficulty: Medium
# Approach: Greedy (Largest to smallest values)
# Time Complexity: O(1)  (fixed set of roman values)
# Space Complexity: O(1)
#
# Explanation:
# Use a list of (value, symbol) pairs from largest to smallest (including subtractive forms).
# Repeatedly take the largest value <= num, append its symbol, subtract value, and continue.

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        result = []

        for value, symbol in values:
            while num >= value:
                result.append(symbol)
                num -= value

        return "".join(result)
IntegerToRoman.py
