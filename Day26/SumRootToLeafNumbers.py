# LeetCode: Sum Root to Leaf Numbers
# Difficulty: Medium
# Approach: DFS (Recursion)
# Time Complexity: O(n)
# Space Complexity: O(h) where h is height of tree
#
# Explanation:
# - Traverse from root to leaf.
# - Build the number by multiplying previous path by 10 and adding node value.
# - When a leaf node is reached, return the formed number.
# - Sum all root-to-leaf numbers.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return 0

            path = path * 10 + node.val

            if not node.left and not node.right:
                return path

            return dfs(node.left, path) + dfs(node.right, path)

        return dfs(root, 0)
