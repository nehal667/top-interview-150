# LeetCode: Insert Interval
# Difficulty: Medium
# Approach: Linear Scan + Merge
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# 1. Add all intervals that end before the new interval starts.
# 2. Merge all overlapping intervals with the new interval.
# 3. Add remaining intervals after the merged interval.

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0

        # Add intervals before newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1])
            ]
            i += 1
        merged.append(newInterval)

        # Add remaining intervals
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1

        return merged
