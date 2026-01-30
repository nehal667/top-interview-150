# LeetCode: Linked List Cycle
# Difficulty: Easy
# Approach: Floyd’s Cycle Detection (Two Pointers)
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# Use two pointers:
# - slow moves one step
# - fast moves two steps
# If they meet → cycle exists.
# If fast reaches None → no cycle.

class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
