# Day 29: Remove Element (LeetCode #27)
# Technique: Fast & Slow (Read/Write) Pointers
# Logic: Overwrite elements we want to remove to achieve O(1) Space.

class Solution(object):
    def removeElement(self, nums, val):
        # 'l' is the slow writer pointer
        l = 0

        # 'r' is the fast reader pointer
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
                
        return l