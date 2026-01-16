# Day 19: Subsets II (LeetCode #90)
# Topic: Backtracking with Duplicate Pruning
# Strategy: Sort + Skip siblings in the decision tree

class Solution(object):
    def subsetsWithDup(self, nums):
        # 1. Sort is mandatory to put duplicates next to each other
        nums.sort()
        res = []

        def helper(strt, curr_path):
            # 2. Every node in the decision tree is a valid subset
            # (Unlike others, we don't wait for a specific length or sum)
            res.append(list(curr_path))
            
            for i in range(strt, len(nums)):
                # 3. Duplicate Handling: 
                # If the current number is the same as the previous one
                # in THIS specific loop, we skip it to avoid a clone branch.
                if i > strt and nums[i] == nums[i-1]:
                    continue
                
                # Include
                curr_path.append(nums[i])
                # Move to next index
                helper(i + 1, curr_path)
                # Backtrack
                curr_path.pop()

        helper(0, [])
        return res