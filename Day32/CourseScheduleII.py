# LeetCode: Course Schedule II
# Difficulty: Medium
# Approach: Topological Sort (Kahn’s Algorithm - BFS)
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
#
# Explanation:
# - Build a graph where an edge pre -> course means course depends on pre.
# - Track indegree (number of prerequisites) for each course.
# - Start with courses having indegree 0 (no prerequisites).
# - Repeatedly remove such courses and reduce indegree of neighbors.
# - If all courses are processed, return the order; otherwise return [].

from typing import List
import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Adjacency list and indegree array
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build the graph
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        # Queue of courses with no prerequisites
        queue = collections.deque(
            [i for i in range(numCourses) if indegree[i] == 0]
        )

        result = []

        # BFS Topological Sort
        while queue:
            curr = queue.popleft()
            result.append(curr)

            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If all courses are included, return order; else return empty list
        return result if len(result) == numCourses else []
