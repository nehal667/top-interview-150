# LeetCode: Ransom Note
# Difficulty: Easy
# Approach: Counter (frequency matching)
# Time Complexity: O(n + m)
# Space Complexity: O(1) (26 letters)
#
# Explanation:
# Count letters in ransomNote and magazine using Counter.
# st1 & st2 keeps the minimum counts (intersection).
# If intersection equals st1, magazine contains all required letters.

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        st1 = Counter(ransomNote)
        st2 = Counter(magazine)
        return (st1 & st2) == st1
