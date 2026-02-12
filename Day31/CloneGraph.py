# LeetCode: Clone Graph
# Difficulty: Medium
# Approach: DFS + HashMap
# Time Complexity: O(N + E)
# Space Complexity: O(N)
#
# Explanation:
# - Use DFS to traverse the graph.
# - Use a hashmap to store already cloned nodes to avoid cycles.
# - For each node, create a copy and recursively clone its neighbors.

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        copied = {}

        def dfs(curr: 'Node') -> 'Node':
            # If node already cloned, return it
            if curr in copied:
                return copied[curr]

            # Clone the current node
            clone = Node(curr.val)
            copied[curr] = clone

            # Clone all neighbors
            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
