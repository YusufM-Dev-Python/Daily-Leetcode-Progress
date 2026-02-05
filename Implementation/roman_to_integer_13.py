class Solution(object):
    def romanToInt(self, s):
        # Hash map for O(1) character lookup
        mapi = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0

        for i in range(len(s)):
            curr_val = mapi[s[i]]

            # Look-Ahead Logic:
            # If a smaller value precedes a larger value (like IV or XC),
            # we subtract the smaller value from the total.
            if i + 1 < len(s) and curr_val < mapi[s[i+1]]:
                total -= curr_val
            else:
                total += curr_val
                
        return total