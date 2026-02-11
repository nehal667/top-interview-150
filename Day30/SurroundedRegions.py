# LeetCode: Surrounded Regions
# Difficulty: Medium
# Approach: DFS from Boundary
# Time Complexity: O(m * n)
# Space Complexity: O(m * n) (recursion stack)
#
# Explanation:
# - Any 'O' connected to the boundary cannot be captured.
# - First, mark all boundary-connected 'O's as temporary 'T'.
# - Convert remaining 'O's to 'X'.
# - Convert 'T's back to 'O'.

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rlen = len(board)
        clen = len(board[0])

        def capture(r: int, c: int) -> None:
            if r < 0 or r >= rlen or c < 0 or c >= clen or board[r][c] != "O":
                return

            board[r][c] = "T"

            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Capture boundary-connected regions
        for r in range(rlen):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][clen - 1] == "O":
                capture(r, clen - 1)

        for c in range(clen):
            if board[0][c] == "O":
                capture(0, c)
            if board[rlen - 1][c] == "O":
                capture(rlen - 1, c)

        # Flip surrounded regions
        for r in range(rlen):
            for c in range(clen):
                if board[r][c] == "T":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"
