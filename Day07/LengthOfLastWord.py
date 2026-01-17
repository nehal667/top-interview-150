# LeetCode: Length of Last Word
# Difficulty: Easy
# Approach: Strip + Split
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# - strip() removes leading/trailing spaces
# - split() separates the string into words
# - the last word is words[-1]

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()

        if not words:
            return 0

        return len(words[-1])
