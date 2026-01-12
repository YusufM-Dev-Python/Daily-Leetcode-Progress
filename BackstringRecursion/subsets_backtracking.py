# Day 15: Subsets (LeetCode #78)
# Topic: Backtracking & Decision Trees
# Time Complexity: O(2^n) - Every element has 2 choices (In/Out)
# Space Complexity: O(n) - Depth of the recursion tree

class Solution(object):
    def subsets(self, nums):
        res = []

        def helper(index, curr_list):
            # 1. Base Case: If we've made a decision for every number
            if index == len(nums):
                # We take a "Snapshot" (copy) because curr_list is mutable
                res.append(list(curr_list))
                return 

            # 2. DECISION 1: EXCLUDE nums[index]
            # We move to the next index without adding anything
            helper(index + 1, curr_list)

            # 3. DECISION 2: INCLUDE nums[index]
            # We add the number and move to the next index
            curr_list.append(nums[index])
            helper(index + 1, curr_list)
            
            # 4. BACKTRACK (The "Pop"):
            # We remove the filter to return the list to its original state
            # so the other branches of the tree aren't messed up.
            curr_list.pop()

        helper(0, [])
        return res