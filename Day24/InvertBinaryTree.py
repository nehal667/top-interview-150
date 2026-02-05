# LeetCode: Invert Binary Tree
# Difficulty: Easy
# Approach: Recursion (DFS)
# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the tree
#
# Explanation:
# - If the current node is None, return.
# - Swap the left and right child of the node.
# - Recursively invert left and right subtrees.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap left and right children
        root.left, root.right = root.right, root.left

        # Recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
