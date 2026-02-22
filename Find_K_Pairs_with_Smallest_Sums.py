# Day 41 - Find K Pairs with Smallest Sums
# LeetCode Problem

import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        resV = []  # Result list
        pq = []    # Min heap

        # Push initial pairs into heap
        for x in nums1:
            heapq.heappush(pq, [x + nums2[0], 0])

        # Extract k smallest pairs
        while k > 0 and pq:
            s, pos = heapq.heappop(pq)

            resV.append([s - nums2[pos], nums2[pos]])

            # Push next element from nums2
            if pos + 1 < len(nums2):
                heapq.heappush(
                    pq,
                    [s - nums2[pos] + nums2[pos + 1], pos + 1]
                )

            k -= 1

        return resV
