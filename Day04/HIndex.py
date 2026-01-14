# LeetCode: H-Index
# Difficulty: Medium
# Approach: Sort (Descending) + Count valid papers
# Time Complexity: O(n log n)
# Space Complexity: O(1) extra space (ignoring sorting internals)
#
# Explanation:
# Sort citations in descending order.
# For each position i, check if citations[i] >= i + 1.
# If true, it means we have (i+1) papers with at least (i+1) citations each.
# When it becomes false, we stop because remaining citations are smaller.

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        count = 0
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                count += 1
            else:
                break

        return count
