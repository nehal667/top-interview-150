# LeetCode: Find the Index of the First Occurrence in a String
# Difficulty: Easy
# Approach: Sliding Window (Substring Comparison)
# Time Complexity: O((n - m + 1) * m) in worst case
# Space Complexity: O(1)
#
# Explanation:
# Check each possible starting index i in haystack.
# Compare haystack[i : i + len(needle)] with needle.
# If they match, return i. Otherwise, return -1.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)

        for i in range(len(haystack)):
            if haystack[i:i + n] == needle:
                return i

        return -1
