# LeetCode: Rotate List
# Difficulty: Medium
# Approach: Linked List Length + Re-linking
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# - Find the length of the list.
# - Make the list circular.
# - Break the circle at the correct position to form the rotated list.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        length = 1
        tail = head

        # Find the length and tail
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        # Find the new tail
        current = head
        for _ in range(length - k - 1):
            current = current.next

        new_head = current.next
        current.next = None
        tail.next = head

        return new_head
