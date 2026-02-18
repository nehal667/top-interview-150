# LeetCode: Merge k Sorted Lists
# Difficulty: Hard
# Approach: Min Heap (Priority Queue)
#
# Idea:
# - Push the head of each linked list into a min-heap.
# - Always extract the smallest node and push its next node into the heap.
# - Continue until the heap is empty.
#
# Time Complexity:
#   O(N log k), where N is total number of nodes and k is number of lists
# Space Complexity:
#   O(k) for the heap

import heapq
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Push the head of each list into the heap
        for i, node in enumerate(lists):
            if node:
                # (value, index, node) ensures proper comparison
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy
        
        # Extract the smallest node and push its next
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
