# LeetCode: Isomorphic Strings
# Difficulty: Easy
# Approach: Two HashMaps (bidirectional mapping)
# Time Complexity: O(n)
# Space Complexity: O(1) / O(n) depending on charset
#
# Explanation:
# Maintain mapping s->t and t->s.
# If a character was mapped before, it must map to the same character again.
# Two different characters cannot map to the same character.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for cs, ct in zip(s, t):
            if cs in s_to_t and s_to_t[cs] != ct:
                return False
            if ct in t_to_s and t_to_s[ct] != cs:
                return False

            s_to_t[cs] = ct
            t_to_s[ct] = cs

        return True
