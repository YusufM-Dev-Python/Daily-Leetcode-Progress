# Day 16: Permutations
# Topic: Backtracking (Exploration of all possible orderings)
# Time Complexity: O(n! * n)
# Space Complexity: O(n)

class Solution(object):
    def permute(self, nums):
        res = []

        def backing(curr_path):
            # 1. Base Case: If the path length equals nums length, 
            # we've used every number exactly once.
            if len(curr_path) == len(nums):
                res.append(list(curr_path))
                return

            # 2. Why no index? Because for every "slot" in our permutation, 
            # we are allowed to pick ANY number from the original list...
            for n in nums:
                # ...AS LONG AS we haven't used it already in the current path.
                if n in curr_path:
                    continue
                
                # Choose
                curr_path.append(n)

                # Explore (Notice: no index+1 here, we always scan all nums)
                backing(curr_path)

                # Un-choose (Backtrack)
                curr_path.pop()

        backing([])
        return res