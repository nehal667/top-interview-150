# LeetCode: Validate Binary Search Tree
# Difficulty: Medium
# Approach: DFS with Range Validation
# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the tree
#
# Explanation:
# - For a BST, every node must satisfy:
#     left subtree values < node.val < right subtree values
# - Maintain a valid range (min, max) for each node.
# - Recursively validate left and right subtrees with updated ranges.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node: Optional[TreeNode], minimum: float, maximum: float) -> bool:
            if not node:
                return True

            if not (minimum < node.val < maximum):
                return False

            return (
                valid(node.left, minimum, node.val) and
                valid(node.right, node.val, maximum)
            )

        return valid(root, float("-inf"), float("inf"))

