# LeetCode: Minimum Window Substring
# Difficulty: Hard
# Approach: Sliding Window + Frequency Array (ASCII)
# Time Complexity: O(n)
# Space Complexity: O(1)  (fixed size 128 array)
#
# Explanation:
# - Build frequency needs for string t using an array of size 128.
# - Expand the window with 'end' until all required characters are included.
# - Then shrink from 'start' to get the minimum window.
# - Track the best window length and starting index.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        freq = [0] * 128
        count = len(t)

        start = 0
        end = 0
        min_len = float("inf")
        start_index = 0

        # Count needed characters from t
        for ch in t:
            freq[ord(ch)] += 1

        while end < len(s):
            if freq[ord(s[end])] > 0:
                count -= 1
            freq[ord(s[end])] -= 1
            end += 1

            # When we have all characters, try to shrink from the left
            while count == 0:
                if end - start < min_len:
                    start_index = start
                    min_len = end - start

                if freq[ord(s[start])] == 0:
                    count += 1
                freq[ord(s[start])] += 1
                start += 1

        return "" if min_len == float("inf") else s[start_index:start_index + min_len]
