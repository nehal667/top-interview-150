# Day 41 - IPO (Maximized Capital)
# LeetCode Problem

from typing import List
import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:

        n = len(profits)

        # Pair capital and profit
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()

        maxHeap = []
        i = 0

        # Select at most k projects
        for _ in range(k):

            # Push all affordable projects into max heap
            while i < n and projects[i][0] <= w:
                heapq.heappush(maxHeap, -projects[i][1])
                i += 1

            if not maxHeap:
                break

            # Add highest profit project
            w -= heapq.heappop(maxHeap)

        return w
