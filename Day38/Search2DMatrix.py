# LeetCode: Search a 2D Matrix
# Difficulty: Medium
#
# Approach:
# 1. Use Binary Search to find the correct row.
# 2. Apply Binary Search again inside that row.
#
# Time Complexity: O(log(m) + log(n))
# Space Complexity: O(1)

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Step 1: Binary search to find correct row
        top = 0
        bot = len(matrix) - 1

        while top <= bot:
            mid = (top + bot) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                top = mid + 1
        
        # Row where target may exist
        row = (top + bot) // 2

        # Step 2: Binary search inside the row
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
