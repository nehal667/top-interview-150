# Day 44 - Palindrome Number
# LeetCode Problem

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert number to string and compare with reverse
        return str(x) == str(x)[::-1]
