# LeetCode: Binary Tree Right Side View
# Difficulty: Medium
# Approach: Breadth-First Search (Level Order Traversal)
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# - Perform level-order traversal using a queue.
# - For each level, track the last (rightmost) node.
# - Add the value of the rightmost node to the result list.

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        q = deque([root])

        while q:
            right_side = None
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                right_side = node

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Add the rightmost node of the current level
            res.append(right_side.val)

        return res
