# LeetCode: Contains Duplicate II
# Difficulty: Easy
# Approach: HashMap (store last seen index)
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Explanation:
# Keep a dictionary that stores the last index where each number appeared.
# When we see the number again at index idx:
# - check if idx - last_index <= k
# If yes -> return True, otherwise update last_index.

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for idx in range(len(nums)):
            if nums[idx] in last_seen and idx - last_seen[nums[idx]] <= k:
                return True
            last_seen[nums[idx]] = idx

        return False
