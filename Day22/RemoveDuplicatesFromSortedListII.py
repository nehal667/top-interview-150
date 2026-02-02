# LeetCode: Remove Duplicates from Sorted List II
# Difficulty: Medium
# Approach: Two Pointers + Dummy Node
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# - Use a dummy node to handle edge cases (duplicates at head).
# - Traverse the list using two pointers.
# - If duplicates are found, skip all nodes with that value.
# - Otherwise, move pointers normally.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                # Skip all nodes with the same value
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next

        return dummy.next
