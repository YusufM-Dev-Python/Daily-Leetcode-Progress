# Day 20: Permutations II
# Topic: Backtracking with Duplicates and State Tracking
# Logic: Use a 'used' array to track indices and sort to prune duplicate values.

class Solution(object):
    def permuteUnique(self, nums):
        res = []
        nums.sort()  # 1. Essential for grouping duplicates
        used = [False] * len(nums) # 2. Track specific indices

        def helper(curr_path):
            if len(curr_path) == len(nums):
                res.append(list(curr_path))
                return

            for i in range(len(nums)):
                # 3. Index Constraint: Don't use the same physical index twice
                if used[i]:
                    continue
                
                # 4. THE MAGIC LINE (Duplicate Pruning):
                # If this number is same as previous, and the previous WAS NOT used
                # in this path, it means we are about to start a duplicate branch.
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue 
                
                # Choose
                used[i] = True
                curr_path.append(nums[i])
                
                # Explore
                helper(curr_path)

                # Backtrack
                curr_path.pop()
                used[i] = False
                
        helper([])
        return res