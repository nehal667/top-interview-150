# LeetCode: Minimum Absolute Difference in BST
# Difficulty: Easy
# Approach: Inorder Traversal (DFS)
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# - Inorder traversal of a BST gives sorted values.
# - The minimum absolute difference will be between adjacent elements.
# - Traverse the tree, store values, then compute the minimum difference.

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root: Optional[TreeNode], arr: List[int]) -> None:
        if not root:
            return
        self.dfs(root.left, arr)
        arr.append(root.val)
        self.dfs(root.right, arr)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        self.dfs(root, arr)

        min_diff = float('inf')
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i - 1])

        return min_diff
