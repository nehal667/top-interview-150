# LeetCode: Flatten Binary Tree to Linked List
# Difficulty: Medium
# Approach: Iterative (Morris Traversal style)
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# - Traverse the tree starting from root.
# - If a node has a left child:
#   - Find the rightmost node of the left subtree.
#   - Attach the current node's right subtree to it.
#   - Move the left subtree to the right.
#   - Set left child to None.
# - Move to the next right node.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root

        while curr:
            if curr.left:
                # Find the rightmost node of left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right

                # Rewire connections
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None

            curr = curr.right
