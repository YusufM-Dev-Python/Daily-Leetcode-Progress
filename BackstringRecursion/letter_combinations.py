# Day 16: Letter Combinations of a Phone Number
# Topic: Backtracking / Depth First Search
# Complexity: O(4^n * n) - where n is length of digits

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        # The Phone Keypad Mapping
        mappi = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", 
                 '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        res = []

        def helper(i, cur_str):
            # 1. Base Case: If the string we are building is 
            # as long as the input digits, we found a combination.
            if len(cur_str) == len(digits):
                res.append(cur_str)
                return 

            # 2. Recursive Step: Look at the current digit (digits[i])
            # and loop through all possible letters it can represent.
            for char in mappi[digits[i]]:
                # We move to the next digit (i+1) and 
                # "Join" the current character to our path.
                helper(i + 1, cur_str + char) 

        helper(0, "") 
        return res