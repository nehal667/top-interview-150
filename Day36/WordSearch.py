# LeetCode: Word Search
# Difficulty: Medium
# Approach: Backtracking + DFS
#
# Idea:
# - Start DFS from every cell.
# - Match characters of the word one by one.
# - Mark the cell as visited temporarily to avoid reuse.
# - Backtrack after exploring all paths.
#
# Time Complexity:
#   O(m * n * 4^L), where L is length of the word
# Space Complexity:
#   O(L) recursion stack

class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def backtrack(i, j, k):
            # If all characters are matched
            if k == len(word):
                return True
            
            # Out of bounds or mismatch
            if (i < 0 or i >= rows or 
                j < 0 or j >= cols or 
                board[i][j] != word[k]):
                return False
            
            # Mark current cell as visited
            temp = board[i][j]
            board[i][j] = "#"
            
            # Explore all 4 directions
            found = (
                backtrack(i + 1, j, k + 1) or
                backtrack(i - 1, j, k + 1) or
                backtrack(i, j + 1, k + 1) or
                backtrack(i, j - 1, k + 1)
            )
            
            # Backtrack (restore value)
            board[i][j] = temp
            return found

        # Try starting DFS from each cell
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        
        return False
