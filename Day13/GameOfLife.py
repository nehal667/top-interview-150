# LeetCode: Game of Life
# Difficulty: Medium
# Approach: In-place state encoding
# Time Complexity: O(m * n)
# Space Complexity: O(1)
#
# Explanation:
# We update the board in-place using temporary markers:
# - -1 means cell was alive (1) but will die (0)
# -  2 means cell was dead (0) but will become alive (1)
# While counting neighbors, use abs(board[r][c]) == 1 to treat -1 as originally alive.
# After first pass, convert:
# - values > 0 -> 1
# - values <= 0 -> 0

from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        directions = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
        m, n = len(board), len(board[0])

        # First pass: mark transitions using -1 and 2
        for i in range(m):
            for j in range(n):
                live = 0

                for x, y in directions:
                    r, c = i + x, j + y
                    if 0 <= r < m and 0 <= c < n and abs(board[r][c]) == 1:
                        live += 1

                if board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = -1     # alive -> dead
                elif board[i][j] == 0 and live == 3:
                    board[i][j] = 2      # dead -> alive

        # Second pass: finalize states
        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if board[i][j] > 0 else 0
