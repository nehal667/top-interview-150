# LeetCode: Ransom Note
# Difficulty: Easy
# Approach: Frequency Count (26 letters)
# Time Complexity: O(n + m)
# Space Complexity: O(1)
#
# Explanation:
# Count letters in magazine. For each letter in ransomNote, decrease the count.
# If any count goes below 0, magazine doesn't have enough letters.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = [0] * 26

        for ch in magazine:
            freq[ord(ch) - ord('a')] += 1

        for ch in ransomNote:
            idx = ord(ch) - ord('a')
            freq[idx] -= 1
            if freq[idx] < 0:
                return False

        return True
