# LeetCode: Kth Smallest Element in a BST
# Difficulty: Medium
# Approach: Inorder Traversal (DFS)
# Time Complexity: O(n)
# Space Complexity: O(h) where h is height of the tree
#
# Explanation:
# - Inorder traversal of a BST gives nodes in sorted order.
# - Count nodes as we traverse.
# - When count reaches k, store the result.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = None

        def inorder(node: Optional[TreeNode]):
            if not node or self.res is not None:
                return

            inorder(node.left)

            self.count += 1
            if self.count == k:
                self.res = node
                return

            inorder(node.right)

        inorder(root)
        return self.res.val
