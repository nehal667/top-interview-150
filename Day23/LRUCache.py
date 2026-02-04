# LeetCode: LRU Cache
# Difficulty: Medium
# Approach: OrderedDict (Hash Map + Doubly Linked List)
# Time Complexity: O(1) for get and put
# Space Complexity: O(capacity)
#
# Explanation:
# - OrderedDict keeps elements in insertion order.
# - Recently used keys are moved to the end.
# - Least recently used key is removed when capacity is exceeded.

from collections import OrderedDict
from typing import Dict

class LRUCache:
    __slots__ = ('data', 'capacity')

    def __init__(self, capacity: int):
        self.data: Dict[int, int] = OrderedDict()
        self.capacity: int = capacity

    def get(self, key: int) -> int:
        # If key not present, return -1
        if key not in self.data:
            return -1
        
        # Move key to end (most recently used)
        value = self.data.pop(key)
        self.data[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        # If key exists, update and move to end
        if key in self.data:
            self.data.pop(key)
        
        self.data[key] = value

        # If capacity exceeded, remove least recently used item
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)
