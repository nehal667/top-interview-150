# LeetCode: Evaluate Division
# Difficulty: Medium
# Approach: Graph + DFS
# Time Complexity: O(N + Q * (V + E))
# Space Complexity: O(V + E)
#
# Explanation:
# - Treat each variable as a node in a graph.
# - Each equation creates two directed edges with weights.
# - For each query, perform DFS to find a path and multiply edge weights.

from typing import List, Dict, Set


class Solution:
    def dfs(
        self,
        node: str,
        dest: str,
        graph: Dict[str, Dict[str, float]],
        visited: Set[str],
        ans: List[float],
        curr_val: float
    ) -> None:
        if node in visited:
            return

        visited.add(node)

        if node == dest:
            ans[0] = curr_val
            return

        for neighbor, value in graph[node].items():
            self.dfs(neighbor, dest, graph, visited, ans, curr_val * value)

    def buildGraph(self, equations: List[List[str]], values: List[float]) -> Dict[str, Dict[str, float]]:
        graph = {}

        for i in range(len(equations)):
            dividend, divisor = equations[i]
            value = values[i]

            if dividend not in graph:
                graph[dividend] = {}
            if divisor not in graph:
                graph[divisor] = {}

            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1.0 / value

        return graph

    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:

        graph = self.buildGraph(equations, values)
        result = []

        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                result.append(-1.0)
            else:
                visited = set()
                ans = [-1.0]
                self.dfs(dividend, divisor, graph, visited, ans, 1.0)
                result.append(ans[0])

        return result
