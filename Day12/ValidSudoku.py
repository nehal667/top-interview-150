# LeetCode: Valid Sudoku
# Difficulty: Medium
# Approach: Boolean tracking for rows, columns, and 3x3 boxes
# Time Complexity: O(81) -> O(1)
# Space Complexity: O(1)
#
# Explanation:
# Use three 9x9 boolean arrays:
# - rows[i][num]  -> whether num has appeared in row i
# - cols[j][num]  -> whether num has appeared in column j
# - boxes[b][num] -> whether num has appeared in 3x3 box b
# If a number repeats in any row/col/box, return False.

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = ord(board[i][j]) - ord('1')          # '1'..'9' -> 0..8
                    box_index = (i // 3) * 3 + (j // 3)        # which 3x3 box

                    if rows[i][num] or cols[j][num] or boxes[box_index][num]:
                        return False

                    rows[i][num] = cols[j][num] = boxes[box_index][num] = True

        return True
