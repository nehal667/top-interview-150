# LeetCode: Set Matrix Zeroes
# Difficulty: Medium
# Approach: Constant Space (Use first row/column as markers)
# Time Complexity: O(m*n)
# Space Complexity: O(1)
#
# Explanation:
# - If a cell is 0, its entire row and column must become 0.
# - Use the first row to mark which columns should be zero.
# - Use the first column to mark which rows should be zero.
# - Keep two flags to remember if the first row / first column originally had any zeros.

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        # Check if first row / first column originally contains a zero
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Use first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set cells to zero using markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero out first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
