# LeetCode: Populating Next Right Pointers in Each Node
# Difficulty: Medium
# Approach: Breadth-First Search (Level Order Traversal)
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# - Use a queue to perform level-order traversal.
# - For each level, connect nodes from left to right using the `next` pointer.
# - The last node in each level points to None.

from collections import deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: 'Node' = None,
        right: 'Node' = None,
        next: 'Node' = None
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root

        queue = deque([root])

        while queue:
            size = len(queue)
            prev = None

            for _ in range(size):
                node = queue.popleft()

                if prev:
                    prev.next = node
                prev = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Last node in the level points to None
            prev.next = None

        return root
