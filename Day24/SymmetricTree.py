# LeetCode: Symmetric Tree
# Difficulty: Easy
# Approach: Recursion (Mirror Check)
# Time Complexity: O(n)
# Space Complexity: O(h) where h is tree height
#
# Explanation:
# A tree is symmetric if the left subtree is a mirror reflection of the right subtree.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # If tree is empty, it is symmetric
        if not root:
            return True

        return self.isSame(root.left, root.right)

    def isSame(self, leftroot: Optional[TreeNode], rightroot: Optional[TreeNode]) -> bool:
        # Both nodes are None
        if leftroot is None and rightroot is None:
            return True

        # One node is None
        if leftroot is None or rightroot is None:
            return False

        # Values must match
        if leftroot.val != rightroot.val:
            return False

        # Check mirror condition
        return (
            self.isSame(leftroot.left, rightroot.right) and
            self.isSame(leftroot.right, rightroot.left)
        )
