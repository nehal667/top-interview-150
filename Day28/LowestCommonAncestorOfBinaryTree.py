# LeetCode: Lowest Common Ancestor of a Binary Tree
# Difficulty: Medium
# Approach: Recursion (DFS)
# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the tree
#
# Explanation:
# - If the current node is None or equals p or q, return it.
# - Recurse on left and right subtrees.
# - If both sides return non-null, current node is the LCA.
# - Otherwise, return the non-null child.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':

        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right
