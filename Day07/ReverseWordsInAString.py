# LeetCode: Reverse Words in a String
# Difficulty: Medium
# Approach: Split + Reverse + Join
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# - split() separates words and removes extra spaces automatically
# - reverse the list of words
# - join them back with single spaces

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words = words[::-1]
        return " ".join(words)
