# LeetCode: Word Ladder
# Difficulty: Hard
# Approach: BFS (Shortest Path in Unweighted Graph)
# Time Complexity: O(N * L * 26)
# Space Complexity: O(N)
#
# Explanation:
# - Each word is treated as a node in a graph.
# - An edge exists if two words differ by one character.
# - Use BFS to find the shortest transformation sequence.
# - Remove visited words from the set to avoid revisits.

import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = collections.deque([(beginWord, 1)])

        while queue:
            word, dist = queue.popleft()

            if word == endWord:
                return dist

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + ch + word[i + 1:]
                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        queue.append((next_word, dist + 1))

        return 0
