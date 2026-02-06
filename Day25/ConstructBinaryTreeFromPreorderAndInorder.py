# LeetCode: Construct Binary Tree from Preorder and Inorder Traversal
# Difficulty: Medium
# Approach: Recursion + HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# - Preorder traversal gives the root first.
# - Inorder traversal tells us how to split left and right subtrees.
# - Use a hashmap to quickly find the index of a node in inorder.
# - Recursively build left and right subtrees.

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in inorder traversal
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.index = 0

        def helper(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None

            # Pick current root from preorder
            root_val = preorder[self.index]
            self.index += 1
            root = TreeNode(root_val)

            # Split inorder list
            mid = idx_map[root_val]

            # Build left and right subtrees
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)

            return root

        return helper(0, len(inorder) - 1)
