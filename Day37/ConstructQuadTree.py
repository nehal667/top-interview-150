# LeetCode: Construct Quad Tree
# Difficulty: Medium
# Approach: Divide and Conquer (Recursion)
#
# Idea:
# - Recursively divide the grid into 4 equal parts.
# - If all 4 sub-grids are leaf nodes with the same value,
#   merge them into a single leaf node.
# - Otherwise, create an internal node with 4 children.
#
# Time Complexity: O(n^2)
# Space Complexity: O(log n) recursion stack

from typing import List

# Definition for a QuadTree node.
# class Node:
#     def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
#         self.val = val
#         self.isLeaf = isLeaf
#         self.topLeft = topLeft
#         self.topRight = topRight
#         self.bottomLeft = bottomLeft
#         self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def construct_range(top: int, left: int, length: int) -> 'Node':
            # Base case: single cell
            if length == 1:
                return Node(grid[top][left], True)
            
            half = length // 2
            
            topLeft = construct_range(top, left, half)
            topRight = construct_range(top, left + half, half)
            bottomLeft = construct_range(top + half, left, half)
            bottomRight = construct_range(top + half, left + half, half)

            # If all children are leaf nodes with same value, merge them
            if (
                topLeft.isLeaf and topRight.isLeaf and
                bottomLeft.isLeaf and bottomRight.isLeaf and
                topLeft.val == topRight.val ==
                bottomLeft.val == bottomRight.val
            ):
                return Node(topLeft.val, True)
            
            # Otherwise create an internal node
            return Node(
                0,
                False,
                topLeft,
                topRight,
                bottomLeft,
                bottomRight
            )
        
        return construct_range(0, 0, len(grid))
