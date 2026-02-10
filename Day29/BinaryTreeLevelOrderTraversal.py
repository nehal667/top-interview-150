# LeetCode: Binary Tree Level Order Traversal
# Difficulty: Medium
# Approach: Breadth-First Search (Level Order Traversal)
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# - Use a queue to traverse the tree level by level.
# - Maintain a temporary queue to store nodes of the next level.
# - Append values of each level into the result list.

from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        levels = []

        while queue:
            level = []
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels.append(level)

        return levels
