# LeetCode: Letter Combinations of a Phone Number
# Difficulty: Medium
# Approach: Backtracking
#
# Idea:
# - Each digit maps to a set of characters (like a phone keypad).
# - Use backtracking to try all possible combinations.
# - Build the string step by step and store it when complete.
#
# Time Complexity:
#   O(4^n) where n is the length of digits
# Space Complexity:
#   O(n) for recursion stack

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        res = []

        def backtrack(idx: int, comb: str) -> None:
            # If current combination length equals digits length
            if idx == len(digits):
                res.append(comb)
                return
            
            # Try all letters mapped to current digit
            for letter in digit_to_letters[digits[idx]]:
                backtrack(idx + 1, comb + letter)

        backtrack(0, "")
        return res
