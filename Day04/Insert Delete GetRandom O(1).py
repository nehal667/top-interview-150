# LeetCode: Insert Delete GetRandom O(1)
# Difficulty: Medium
# Approach: Array + Hash Map (value -> index)
# Time Complexity: O(1) average for insert, remove, getRandom
# Space Complexity: O(n)
#
# Explanation:
# - Use a list to store values (allows O(1) random access for getRandom).
# - Use a dictionary to store each value’s index in the list (allows O(1) lookup).
# - For remove, swap the element to delete with the last element, then pop.

import random
from typing import List

class RandomizedSet:

    def __init__(self):
        self.nums_index = {}  # val -> index in self.nums
        self.nums: List[int] = []

    def insert(self, val: int) -> bool:
        if val in self.nums_index:
            return False
        self.nums_index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.nums_index:
            return False

        idx = self.nums_index[val]
        last_element = self.nums[-1]

        # Move last element into the position of the element to remove
        self.nums[idx] = last_element
        self.nums_index[last_element] = idx

        # Remove last element and delete val from dictionary
        self.nums.pop()
        del self.nums_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
