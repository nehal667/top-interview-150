# LeetCode: Add Two Numbers
# Difficulty: Medium
# Approach: Linked List Simulation with Carry
# Time Complexity: O(max(n, m))
# Space Complexity: O(max(n, m))
#
# Explanation:
# Each linked list stores a number in reverse order.
# Add digit-by-digit with carry, create a new result list.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            digit = total % 10

            cur.next = ListNode(digit)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
