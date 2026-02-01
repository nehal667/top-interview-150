# LeetCode: Copy List with Random Pointer
# Difficulty: Medium
# Approach: HashMap (Old Node → New Node)
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# 1. First pass: Create a copy of each node and store mapping (old → new).
# 2. Second pass: Assign next and random pointers using the mapping.
# 3. Return the copied head node.

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        old_to_new = {}

        # First pass: create new nodes
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: assign next and random pointers
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]
