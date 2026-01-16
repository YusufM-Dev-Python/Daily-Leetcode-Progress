# Day 19 (Part 2): Combination Sum III
# Topic: Backtracking with Multiple Constraints (Sum + Length)
# Rule: Use only digits 1-9, each at most once.

class Solution(object):
    def combinationSum3(self, k, n):
        res = []
            
        def helper(strt, curr_path, curr_sum):
            # 1. Double Success Condition: 
            # We hit the target sum AND the exact number of elements (k).
            if curr_sum == n and len(curr_path) == k:
                res.append(list(curr_path))
                return 
            
            # 2. Pruning: If we exceed the sum OR the allowed length, stop.
            if curr_sum > n or len(curr_path) > k:
                return 

            # 3. The Range: Problem specifies digits 1 through 9.
            for i in range(strt, 10):
                # Choose
                curr_path.append(i)
                # Explore (i + 1 ensures we don't reuse the same digit)
                helper(i + 1, curr_path, curr_sum + i)
                # Backtrack
                curr_path.pop()
        
        # Start at 1 per the problem constraints
        helper(1, [], 0)
        return res