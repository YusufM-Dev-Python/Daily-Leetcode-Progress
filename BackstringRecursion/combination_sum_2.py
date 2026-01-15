# Day 17 (Part 2): Combination Sum II (LeetCode #40)
# Topic: Backtracking with Duplicate Handling
# Logic: Each element can only be used once. No duplicate combinations in result.

class Solution(object):
    def combinationSum2(self, candidates, target):
        # 1. CRITICAL: Sort to bring duplicates together
        candidates.sort()
        res = []

        def helper(strt, curr_arr, curr_sum):
            if curr_sum == target:
                res.append(list(curr_arr))
                return 
            
            if curr_sum > target:
                return 

            for i in range(strt, len(candidates)):
                # 2. DUPLICATE HANDLING:
                # If this number is the same as the previous one in THIS loop, skip it.
                # 'i > strt' ensures we don't skip the very first occurrence.
                if i > strt and candidates[i] == candidates[i-1]:
                    continue
                
                # 3. OPTIMIZATION:
                # Since candidates is sorted, if current sum + this number is too big,
                # everything after it will also be too big.
                if curr_sum + candidates[i] > target:
                    break 
                
                curr_arr.append(candidates[i])
                # 4. INDEX HANDLING: Move to i + 1 (cannot reuse same element)
                helper(i + 1, curr_arr, curr_sum + candidates[i])
                curr_arr.pop()

        helper(0, [], 0)
        return res