# LeetCode: Longest Common Prefix
# Difficulty: Easy
# Approach: Sort + Compare First & Last Strings
# Time Complexity: O(n log n) for sorting + O(m) for comparison
# Space Complexity: O(1) extra (ignoring sorting internals)
#
# Explanation:
# After sorting, the common prefix of the entire list must be the common prefix
# between the first and last strings (they are the most different).
# Compare characters until they differ, then return the matched prefix.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()
        first = strs[0]
        last = strs[-1]

        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        return first[:i]
