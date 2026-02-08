# LeetCode: Path Sum
# Difficulty: Easy
# Approach: Recursion (DFS)
# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the tree
#
# Explanation:
# - If the tree is empty, no path exists.
# - If the node is a leaf, check whether the remaining sum equals node value.
# - Otherwise, recursively check left and right subtrees with reduced sum.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # If leaf node, check sum
        if not root.left and not root.right:
            return targetSum == root.val

        # Recur for left and right subtree
        return (
            self.hasPathSum(root.left, targetSum - root.val) or
            self.hasPathSum(root.right, targetSum - root.val)
        )
