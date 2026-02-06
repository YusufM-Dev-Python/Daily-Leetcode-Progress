class Solution(object):
    def twoSum(self, nums, target):
        # Dictionary to store: {value: index}
        mapping = {}

        for i in range(len(nums)):
            n = nums[i]
            diff = target - n

            # Check if the complement already exists in our map
            if diff in mapping:
                return [mapping[diff], i]
            
            # Store the current number and its index for future lookups
            mapping[n] = i