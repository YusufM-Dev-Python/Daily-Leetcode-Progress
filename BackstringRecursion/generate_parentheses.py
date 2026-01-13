# Day 16: Generate Parentheses
# Topic: Backtracking with State Constraints
# Complexity: O(4^n / sqrt(n)) - Catalan Number

class Solution(object):
    def generateParenthesis(self, n):
        res = []

        def helper(curr_str, o_c, c_c):
            # 1. Base Case: Each pair has 2 brackets. 
            # So n pairs = n * 2 total characters.
            if len(curr_str) == n * 2:
                res.append(curr_str)
                return

            # 2. Rule for Opening: We can ALWAYS add '(' 
            # as long as we haven't used up our 'n' limit.
            if o_c < n:
                helper(curr_str + '(', o_c + 1, c_c)

            # 3. Rule for Closing: We can ONLY add ')' 
            # if there is an open bracket waiting to be closed.
            if c_c < o_c:
                helper(curr_str + ')', o_c, c_c + 1)
                
        helper("", 0, 0)
        return res