class Solution(object):
    def threeSum(self, nums):
        nums.sort() # Mandatory for Two Pointers and skipping duplicates
        res = []
        
        for i in range(len(nums)):
            # Skip the same element to avoid duplicate triplets in results
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            
            # The goal is: nums[l] + nums[r] + nums[i] == 0
            # Which is the same as: nums[l] + nums[r] == -nums[i]
            target = -nums[i]
            
            while l < r:
                current_sum = nums[l] + nums[r]
                
                if current_sum == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate values for the second element
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif current_sum > target:
                    r -= 1
                else:
                    l += 1
        return res