class Solution(object):
    def singleNonDuplicate(self, nums):
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            # If mid is even, the partner should be at mid + 1
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    l = mid + 1 # Pattern is correct, unique element is further right
                else:
                    r = mid     # Pattern broke, unique element is at mid or left
            
            # If mid is odd, the partner should be at mid - 1
            else:
                if nums[mid] == nums[mid - 1]:
                    l = mid + 1 # Pattern is correct
                else:
                    r = mid     # Pattern broke
                    
        return nums[l]