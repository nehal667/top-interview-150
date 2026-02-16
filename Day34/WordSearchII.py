# LeetCode: Word Search II
# Difficulty: Hard
# Approach: Trie + Backtracking (DFS)
#
# Idea:
# 1. Build a Trie using the given words.
# 2. Traverse the board using DFS.
# 3. Match characters with Trie nodes.
# 4. Use backtracking to explore all valid paths.
# 5. Mark visited cells to avoid reuse in a single path.
#
# Time Complexity:
#   O(M * N * 4^L) where L is the max word length
# Space Complexity:
#   O(W * L) for Trie + recursion stack

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        rows, cols = len(board), len(board[0])
        result = set()
        visited = set()

        def backtrack(r, c, node, path):
            if node.is_end_of_word:
                result.add(path)
                node.is_end_of_word = False  # avoid duplicates

            visited.add((r, c))

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    ch = board[nr][nc]
                    if ch in node.children:
                        backtrack(nr, nc, node.children[ch], path + ch)

            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                ch = board[r][c]
                if ch in trie.root.children:
                    backtrack(r, c, trie.root.children[ch], ch)

        return list(result)
