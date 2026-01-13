# LeetCode: Best Time to Buy and Sell Stock
# Difficulty: Easy
# Approach: Track minimum price and maximum profit (One Pass)
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# Keep track of the minimum price seen so far (best day to buy).
# For each day, calculate profit if we sell today (price - min_price).
# Update max_profit whenever we find a better profit.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            current_profit = price - min_price

            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit
