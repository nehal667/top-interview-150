# LeetCode: Jump Game
# Difficulty: Medium
# Approach: Greedy (Track farthest reachable index)
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# Keep track of the farthest index we can reach so far (max_reach).
# If at any index i, i is greater than max_reach, it means we cannot reach i,
# so we return False. Otherwise, update max_reach using i + nums[i].

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False

        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])

        return True
