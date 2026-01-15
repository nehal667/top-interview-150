# LeetCode: Gas Station
# Difficulty: Medium
# Approach: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# 1) If total gas < total cost, it's impossible to complete the circuit -> return -1.
# 2) Traverse stations and keep current tank balance (curr_gas).
#    If curr_gas drops below 0 at station i, then we cannot start from the current start index
#    or any station between start and i, so set start = i + 1 and reset curr_gas.

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        curr_gas = 0
        start_idx = 0

        for i in range(len(gas)):
            curr_gas += gas[i] - cost[i]

            if curr_gas < 0:
                curr_gas = 0
                start_idx = i + 1

        return start_idx
