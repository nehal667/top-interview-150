# LeetCode: Best Time to Buy and Sell Stock II
# Difficulty: Medium
# Approach: Greedy (Sum of all upward differences)
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# We can complete as many transactions as we want.
# Whenever today's price is higher than yesterday's, we take that profit.
# Adding all such increases gives the maximum total profit.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit
