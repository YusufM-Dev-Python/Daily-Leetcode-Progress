# Day 13: Insert Delete GetRandom O(1) (LeetCode #380)
# Topic: Data Structure Design (Hybrid Hash Map + List)
# Strategy: "Swap and Pop" logic to maintain O(1) deletions.

import random

class RandomizedSet(object):
    def __init__(self):
        self.map = {}  # Stores {Value : Index}
        self.nums = [] # Stores values for random access

    def insert(self, val):
        if val in self.map:
            return False
        self.map[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        if val not in self.map:
            return False
        
        # Identify the victim's index and the backup (last element)
        idx_remove = self.map[val]
        last_ele = self.nums[-1]

        # 1. Move the last element into the victim's spot
        self.nums[idx_remove] = last_ele
        
        # 2. Update the map to reflect the last element's new index
        self.map[last_ele] = idx_remove

        # 3. Clean up: Pop the end of the list and delete from map
        self.nums.pop()
        del self.map[val]
        return True

    def getRandom(self):
        # random.randint is O(1) and array access is O(1)
        return self.nums[random.randint(0, len(self.nums) - 1)]