class Solution(object):
    def sortColors(self, nums):
        l = 0            # Boundary for 0s
        r = len(nums)-1  # Boundary for 2s
        i = 0            # Current element scanner
        
        while i <= r:
            if nums[i] == 0:
                # Swap 0 to the left boundary
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                # Swap 2 to the right boundary
                # Don't increment i yet, need to check the swapped element
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                # It's a 1, leave it in the middle and move on
                i += 1