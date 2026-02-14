# Day 23: Palindrome Partitioning
# Topic: Backtracking / String Splitting
# Concept: "The Knife" logic for partitioning

class Solution(object):
    def partition(self, s):
        res = []

        # Helper to check if a substring is a palindrome
        def palin(i, j, s):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def helper(i, curr_path):
            # 1. Base Case: If the 'knife' reached the end of the string
            if i >= len(s):
                res.append(list(curr_path))
                return

            # 2. 'j' acts as our knife edge
            for j in range(i, len(s)):
                # 3. Only cut if the piece (from i to j) is a palindrome
                if palin(i, j, s):
                    # Action: Cut the piece s[i:j+1]
                    curr_path.append(s[i:j+1])
                    
                    # 4. Explore: Start next cut AFTER the current piece (j+1)
                    helper(j + 1, curr_path)
                    
                    # Backtrack: Remove the cut and move the knife 'j' further
                    curr_path.pop()

        helper(0, [])
        return res