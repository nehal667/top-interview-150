# LeetCode: Minimum Genetic Mutation
# Difficulty: Medium
# Approach: BFS
# Time Complexity: O(N * 8 * 4)
# Space Complexity: O(N)
#
# Explanation:
# - Each gene string is a node.
# - One mutation = one character change.
# - Use BFS to find the minimum number of mutations.
# - Only valid mutations are those present in the bank.

from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        gene_set = set(bank)

        if endGene not in gene_set and startGene != endGene:
            return -1

        queue = deque([(startGene, 0)])
        visited = {startGene}

        while queue:
            gene, steps = queue.popleft()

            if gene == endGene:
                return steps

            for i in range(8):
                for ch in "ACGT":
                    if gene[i] != ch:
                        new_gene = gene[:i] + ch + gene[i + 1:]
                        if new_gene in gene_set and new_gene not in visited:
                            visited.add(new_gene)
                            queue.append((new_gene, steps + 1))

        return -1
