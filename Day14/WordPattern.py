# LeetCode: Word Pattern
# Difficulty: Easy
# Approach: Set size equality + zip_longest
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# Split s into words.
# If pattern and words follow a one-to-one mapping, then:
# len(set(pattern)) == len(set(words)) == len(set(pairs))
# Using zip_longest also catches cases where lengths differ.

from itertools import zip_longest
from typing import List

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words: List[str] = s.split()

        return (len(set(pattern)) ==
                len(set(words)) ==
                len(set(zip_longest(pattern, words))))
