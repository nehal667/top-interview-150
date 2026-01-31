# LeetCode: Merge Two Sorted Lists
# Difficulty: Easy
# Approach: Concatenate + Extract + Sort + Rewrite
# Time Complexity: O((n+m) log(n+m))
# Space Complexity: O(n+m)
#
# Explanation:
# - Attach list2 to the end of list1
# - Collect all node values into an array
# - Sort the array
# - Write sorted values back into the linked list

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # Move to end of list1
        tail = list1
        while tail.next is not None:
            tail = tail.next

        # Attach list2
        tail.next = list2

        # Collect values
        values = []
        node = list1
        while node:
            values.append(node.val)
            node = node.next

        # Sort values
        values.sort()

        # Write back sorted values
        node = list1
        i = 0
        while node:
            node.val = values[i]
            i += 1
            node = node.next

        return list1
