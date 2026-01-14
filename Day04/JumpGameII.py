# LeetCode: Jump Game II
# Difficulty: Medium
# Approach: Greedy (Range / Level traversal)
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# We keep track of the current jump range [0..end].
# While scanning indices in this range, we compute the farthest index we can reach.
# When we reach the end of the current range, we must take a jump and update end = farthest.
# This guarantees the minimum number of jumps.

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        end = 0
        farthest = 0

        # No need to jump from the last index
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            # Finish current range -> take a jump
            if i == end:
                jumps += 1
                end = farthest

        return jumps
