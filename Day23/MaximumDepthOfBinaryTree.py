# LeetCode: Maximum Depth of Binary Tree
# Difficulty: Easy
# Approach: Recursion (DFS)
# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the tree
#
# Explanation:
# - If the current node is None, depth is 0.
# - Recursively find depth of left and right subtrees.
# - The depth of the tree is 1 + max(left_depth, right_depth).

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)

