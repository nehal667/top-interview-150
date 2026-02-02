# LeetCode: Reverse Nodes in k-Group
# Difficulty: Hard
# Approach: Recursion
# Time Complexity: O(n)
# Space Complexity: O(n) (recursion stack)
#
# Explanation:
# - Reverse nodes in groups of size k
# - If remaining nodes are fewer than k, keep them as is
# - Uses recursion to reverse each group

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        self.n = k
        return self.reverse(head, head, k)
    
    def reverse(
        self,
        head: Optional[ListNode],
        cur: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        if cur is None:
            return None
        
        if k == 1:
            next_group = self.reverse(cur.next, cur.next, self.n)

            if next_group is None:
                head.next = cur.next
            else:
                head.next = next_group

            return cur
        else:
            temp = cur.next
            next_node = self.reverse(head, cur.next, k - 1)

            if next_node is None:
                return None

            temp.next = cur
            return next_node
