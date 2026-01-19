# LeetCode: Is Subsequence
# Difficulty: Easy
# Approach: Two Pointers
# Time Complexity: O(len(t))
# Space Complexity: O(1)
#
# Explanation:
# Use two pointers i (for s) and j (for t).
# Move j through t. When s[i] == t[j], move i forward.
# If i reaches len(s), all characters of s were found in order.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        i = 0
        j = 0

        while j < len(t):
            if i < len(s) and s[i] == t[j]:
                i += 1
            j += 1

            if i == len(s):
                return True

        return i == len(s)
