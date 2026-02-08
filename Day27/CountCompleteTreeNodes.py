# LeetCode: Count Complete Tree Nodes
# Difficulty: Medium
# Approach: Binary Search + Tree Height
# Time Complexity: O((log n)^2)
# Space Complexity: O(1)
#
# Explanation:
# - Compute the height of the tree using left pointers.
# - The last level can have nodes from 1 to 2^h.
# - Use binary search to check how many nodes exist on the last level.
# - Total nodes = nodes above last level + nodes in last level.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Step 1: get height of the tree
        h = 0
        cur = root
        while cur.left:
            cur = cur.left
            h += 1

        # Maximum number of nodes at last level
        max_leaves = 2 ** h

        # Step 2: check if a node exists at given index in last level
        def exists(idx: int) -> bool:
            cur = root
            left, right = 1, max_leaves

            while left < right:
                mid = (left + right) // 2
                if idx > mid:
                    cur = cur.right
                    left = mid + 1
                else:
                    cur = cur.left
                    right = mid

            return cur is not None

        # Step 3: binary search number of nodes in last level
        left, right = 1, max_leaves
        while left <= right:
            mid = (left + right) // 2
            if exists(mid):
                left = mid + 1
            else:
                right = mid - 1

        # Nodes above last level + nodes in last level
        return (2 ** h - 1) + right
