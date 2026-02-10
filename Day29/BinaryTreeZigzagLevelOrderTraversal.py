# LeetCode: Binary Tree Zigzag Level Order Traversal
# Difficulty: Medium
# Approach: BFS using Deque
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# - Use a deque to allow popping from both ends.
# - Traverse level by level.
# - Alternate direction (left-to-right, right-to-left) using a boolean flag.

from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        dq = deque([root])
        reverse = False

        while dq:
            level = []
            size = len(dq)

            for _ in range(size):
                if not reverse:
                    node = dq.popleft()
                    level.append(node.val)
                    if node.left:
                        dq.append(node.left)
                    if node.right:
                        dq.append(node.right)
                else:
                    node = dq.pop()
                    level.append(node.val)
                    if node.right:
                        dq.appendleft(node.right)
                    if node.left:
                        dq.appendleft(node.left)

            res.append(level)
            reverse = not reverse

        return res
