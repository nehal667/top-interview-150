# LeetCode: Group Anagrams
# Difficulty: Medium
# Approach: HashMap with sorted string as key
# Time Complexity: O(n * k log k)  (k = avg word length)
# Space Complexity: O(n)
#
# Explanation:
# Sort each word to create a key. All anagrams share the same sorted key.
# Store words in a dictionary: key -> list of anagrams.

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            res[key].append(word)

        return list(res.values())
