# Day 17: Combination Sum (LeetCode #39)
# Topic: Backtracking with Unlimited Reuse
# Time Complexity: O(2^target) roughly

class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def helper(i, curr_list, total):
            # 1. Base Case: Success! We found a valid combination
            if total == target:
                res.append(list(curr_list))
                return 
            
            # 2. Base Case: Failure! Overshot the target or ran out of numbers
            if total > target or i >= len(candidates):
                return 
            
            # DECISION 1: INCLUDE candidates[i]
            curr_list.append(candidates[i])
            # Key: We stay at index 'i' because we can reuse the same number!
            helper(i, curr_list, total + candidates[i])
            
            # BACKTRACK: Remove the number to explore other possibilities
            curr_list.pop()

            # DECISION 2: EXCLUDE candidates[i]
            # We move to the next index (i + 1) and never look at this candidate again
            helper(i + 1, curr_list, total)

        helper(0, [], 0)
        return res