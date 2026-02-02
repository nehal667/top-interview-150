# LeetCode: Remove Nth Node From End of List
# Difficulty: Medium
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# Use two pointers with a dummy node.
# Move the first pointer n+1 steps ahead.
# Move both pointers until first reaches the end.
# Remove the target node using the second pointer.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy

        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until first reaches the end
        while first is not None:
            first = first.next
            second = second.next

        # Remove the nth node from end
        second.next = second.next.next

        return dummy.next
