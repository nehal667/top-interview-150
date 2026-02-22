# Day 41 - Find Median from Data Stream
# LeetCode Problem

import heapq


class MedianFinder:

    def __init__(self):
        # Max heap (store negatives)
        self.lowerHalf = []

        # Min heap
        self.upperHalf = []

    def addNum(self, num: int) -> None:
        # Add to max heap
        heapq.heappush(self.lowerHalf, -num)

        # Move largest from lowerHalf to upperHalf
        heapq.heappush(self.upperHalf, -heapq.heappop(self.lowerHalf))

        # Maintain size balance
        if len(self.upperHalf) > len(self.lowerHalf):
            heapq.heappush(self.lowerHalf, -heapq.heappop(self.upperHalf))

    def findMedian(self) -> float:
        # Odd number of elements
        if len(self.lowerHalf) > len(self.upperHalf):
            return -self.lowerHalf[0]

        # Even number of elements
        return (-self.lowerHalf[0] + self.upperHalf[0]) / 2.0
