# LeetCode: Binary Tree Maximum Path Sum
# Difficulty: Hard
# Approach: DFS (Recursion)
# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the tree
#
# Explanation:
# - A path can start and end at any node.
# - For each node, calculate the maximum contribution from left and right subtrees.
# - Ignore negative paths using max(0, subtree_sum).
# - Update global result with the maximum path passing through the current node.
# - Return the maximum single-path sum to parent (no split).

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val  # Stores global maximum path sum

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal res

            if not node:
                return 0

            # Maximum path sum from left and right subtrees
            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))

            # Update global maximum (path can split here)
            res = max(res, left_sum + right_sum + node.val)

            # Return max path sum without split
            return max(left_sum, right_sum) + node.val

        dfs(root)
        return res
