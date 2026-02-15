# LeetCode: Implement Trie (Prefix Tree)
# Difficulty: Medium
# Approach: HashMap-based Trie
# Time Complexity:
#   insert: O(L)
#   search: O(L)
#   startsWith: O(L)
# Space Complexity: O(N * L)
#
# Explanation:
# - Each node is a dictionary.
# - '*' is used to mark the end of a word.
# - Traversing characters builds or checks paths in the Trie.

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr['*'] = True   # End of word marker

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter not in curr:
                return False
            curr = curr[letter]
        return '*' in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if letter not in curr:
                return False
            curr = curr[letter]
        return True
