# LeetCode: Same Tree
# Difficulty: Easy
# Approach: Recursion (DFS)
# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the tree
#
# Explanation:
# - If both nodes are None, trees are the same.
# - If one is None and the other is not, trees are different.
# - If values differ, trees are different.
# - Recursively check left and right subtrees.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(
        self,
        p: Optional[TreeNode],
        q: Optional[TreeNode]
    ) -> bool:

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
