# LeetCode: Course Schedule
# Difficulty: Medium
# Approach: DFS + Cycle Detection (Graph)
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
#
# Explanation:
# - Build a graph where each course points to its prerequisites.
# - Use DFS to detect cycles.
# - If a cycle exists, it's impossible to finish all courses.
# - Use a `taken` set to track the current DFS path.

from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)

        # Build graph
        for course, p in prerequisites:
            pre[course].append(p)

        taken = set()

        def dfs(course: int) -> bool:
            # If no prerequisites, course is safe
            if not pre[course]:
                return True

            # Cycle detected
            if course in taken:
                return False

            taken.add(course)

            for p in pre[course]:
                if not dfs(p):
                    return False

            # Mark course as completed
            taken.remove(course)
            pre[course] = []
            return True

        # Check all courses
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
