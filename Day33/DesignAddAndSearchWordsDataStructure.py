# LeetCode: Design Add and Search Words Data Structure
# Difficulty: Medium
# Approach: Trie + DFS (Backtracking)
# Time Complexity:
#   addWord: O(L)
#   search: O(26^L) worst-case (with '.')
# Space Complexity: O(N * L)
#
# Explanation:
# - Use a Trie to store words.
# - For search, use DFS to handle '.' wildcard.
# - '.' can match any character, so we explore all children.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for ch in word:
            current = current.children.setdefault(ch, TrieNode())
        current.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, index: int) -> bool:
            if index == len(word):
                return node.is_word

            ch = word[index]

            if ch == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False

            if ch in node.children:
                return dfs(node.children[ch], index + 1)

            return False

        return dfs(self.root, 0)
