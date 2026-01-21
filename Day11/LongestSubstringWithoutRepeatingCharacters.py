# LeetCode: Longest Substring Without Repeating Characters
# Difficulty: Medium
# Approach: Sliding Window + Set
# Time Complexity: O(n)
# Space Complexity: O(min(n, charset))
#
# Explanation:
# Use a sliding window with two pointers (left, right).
# Keep a set of characters in the current window.
# If a duplicate appears, move left forward and remove characters until the duplicate is gone.
# Track the maximum window length.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        best = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            best = max(best, right - left + 1)

        return best
