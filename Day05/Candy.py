# LeetCode: Candy
# Difficulty: Hard
# Approach: Two Pass Greedy
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# 1) Give every child 1 candy initially.
# 2) Left to Right: if ratings[i] > ratings[i-1], then candies[i] = candies[i-1] + 1.
# 3) Right to Left: if ratings[i] > ratings[i+1], then candies[i] must be at least candies[i+1] + 1.
#    Use max() to keep the larger value from the first pass.
# 4) Sum candies for the minimum total.

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # Left to right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
