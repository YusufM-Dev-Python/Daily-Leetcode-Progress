# Day 28: Search in Rotated Sorted Array (LeetCode #33)
# Topic: Advanced Binary Search
# Logic: One half of the array is ALWAYS sorted.

class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # Left side [l...mid] is sorted
            if nums[l] <= nums[mid]:
                # Is target within this sorted left range?
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # Right side [mid...r] is sorted
            else:
                # Is target within this sorted right range?
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return -1