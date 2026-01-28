# LeetCode: Minimum Number of Arrows to Burst Balloons
# Difficulty: Medium
# Approach: Greedy (Interval Overlap)
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1)
#
# Explanation:
# - Sort balloons by starting point.
# - Track the end of the current overlapping group.
# - If the next balloon starts after the current end, we need a new arrow.
# - Otherwise, shrink the overlap range by updating the end.

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort balloons by starting x-coordinate
        points.sort(key=lambda x: x[0])

        arrows = 1
        end = points[0][1]

        for balloon in points[1:]:
            if balloon[0] > end:
                arrows += 1
                end = balloon[1]
            else:
                end = min(end, balloon[1])

        return arrows
