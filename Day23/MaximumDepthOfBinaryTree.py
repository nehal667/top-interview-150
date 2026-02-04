# LeetCode: Partition List
# Difficulty: Medium
# Approach: Two Linked Lists (Before & After)
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# - Create two dummy lists:
#   1) before → nodes with value < x
#   2) after  → nodes with value >= x
# - Traverse the original list and attach nodes to the correct list.
# - Finally, connect the before list to the after list.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before, after = ListNode(0), ListNode(0)
        before_curr, after_curr = before, after

        while head:
            if head.val < x:
                before_curr.next = head
                before_curr = head
            else:
                after_curr.next = head
                after_curr = head
            head = head.next

        # End the after list
        after_curr.next = None
        # Connect before list with after list
        before_curr.next = after.next

        return before.next
