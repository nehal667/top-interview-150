# LeetCode: Roman to Integer
# Difficulty: Easy
# Approach: Scan + Add/Subtract (based on next symbol)
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# Traverse the string. If the current symbol is smaller than the next symbol,
# subtract it (subtraction rule like IV, IX, XL, etc.). Otherwise, add it.

from typing import Dict

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int: Dict[str, int] = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                result -= roman_to_int[s[i]]
            else:
                result += roman_to_int[s[i]]

        return result
