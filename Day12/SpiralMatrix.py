# LeetCode: Spiral Matrix
# Difficulty: Medium
# Approach: Boundary Pointers (top, bottom, left, right)
# Time Complexity: O(m * n)
# Space Complexity: O(1) extra (excluding output list)
#
# Explanation:
# Maintain four boundaries and traverse:
# 1) left -> right across the top row
# 2) top -> bottom down the right column
# 3) right -> left across the bottom row (if still valid)
# 4) bottom -> top up the left column (if still valid)
# Shrink boundaries after each traversal.

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        spiral: List[int] = []

        while top <= bottom and left <= right:
            # Traverse top row (left -> right)
            for i in range(left, right + 1):
                spiral.append(matrix[top][i])
            top += 1

            # Traverse right column (top -> bottom)
            for j in range(top, bottom + 1):
                spiral.append(matrix[j][right])
            right -= 1

            # Traverse bottom row (right -> left)
            if top <= bottom:
                for k in range(right, left - 1, -1):
                    spiral.append(matrix[bottom][k])
                bottom -= 1

            # Traverse left column (bottom -> top)
            if left <= right:
                for l in range(bottom, top - 1, -1):
                    spiral.append(matrix[l][left])
                left += 1

        return spiral
