# LeetCode: Valid Anagram
# Difficulty: Easy
# Approach: Frequency Array (26 letters)
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# If lengths differ -> not an anagram.
# Use an array of size 26 to count letters.
# Increase count for s[i] and decrease for t[i] in the same loop.
# If all counts end up 0, then both strings have the same letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        arr = [0] * 26

        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] += 1
            arr[ord(t[i]) - ord('a')] -= 1

        for check in arr:
            if check != 0:
                return False

        return True
