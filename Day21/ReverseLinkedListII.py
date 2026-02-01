# LeetCode: Reverse Linked List II
# Difficulty: Medium
# Approach: One-pass in-place reversal
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# Reverse the linked list only between positions left and right.
# Use a dummy node to simplify edge cases.
# Perform in-place reversal by adjusting pointers.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int
    ) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        # Move prev to node before `left`
        for _ in range(left - 1):
            prev = prev.next

        current = prev.next

        # Reverse nodes between left and right
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next
