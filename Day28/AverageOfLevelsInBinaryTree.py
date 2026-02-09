# LeetCode: Average of Levels in Binary Tree
# Difficulty: Easy
# Approach: Breadth-First Search (Level Order Traversal)
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# - Use a queue for level-order traversal.
# - For each level, calculate the sum of node values.
# - Divide the sum by the number of nodes at that level to get the average.

from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level_sum = 0
            count = len(queue)

            for _ in range(count):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level_sum / count)

        return res
