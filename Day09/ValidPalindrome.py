# LeetCode: Valid Palindrome
# Difficulty: Easy
# Approach: Filter + Reverse Check
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# Build a new string containing only alphanumeric characters in lowercase.
# Then compare it with its reverse to check if it's a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        return cleaned == cleaned[::-1]
