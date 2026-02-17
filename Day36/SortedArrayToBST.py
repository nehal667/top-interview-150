# LeetCode: Convert Sorted Array to Binary Search Tree
# Difficulty: Easy
# Approach: Divide and Conquer (Recursion)
#
# Idea:
# - The middle element of the array becomes the root.
# - Left half forms the left subtree.
# - Right half forms the right subtree.
# - This guarantees a height-balanced BST.
#
# Time Complexity:
#   O(n)
# Space Complexity:
#   O(log n) recursion stack (balanced tree)

from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional['TreeNode']:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
