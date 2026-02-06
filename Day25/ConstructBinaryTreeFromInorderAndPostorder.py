# LeetCode: Construct Binary Tree from Inorder and Postorder Traversal
# Difficulty: Medium
# Approach: Recursion
# Time Complexity: O(n^2) due to inorder.index()
# Space Complexity: O(n)
#
# Explanation:
# - The last element of postorder is always the root.
# - Find the root position in inorder to split left and right subtrees.
# - Recursively build left and right subtrees.

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(
        self,
        inorder: List[int],
        postorder: List[int]
    ) -> Optional[TreeNode]:

        if not inorder or not postorder:
            return None

        # Root is last element in postorder
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # Find root index in inorder
        mid = inorder.index(root_val)

        # Build left and right subtrees
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid:-1])

        return root
