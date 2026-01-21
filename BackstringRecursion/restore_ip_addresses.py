# Day 24: Restore IP Addresses
# Pattern: String Partitioning with Multi-Constraints
# Logic: Split string into exactly 4 segments (0-255) without leading zeros.

class Solution(object):
    def restoreIpAddresses(self, s):
        res = []
        
        # Validation Logic: The "Rules" of an IP segment
        def isValid(segment):
            # 1. No leading zeros (unless the segment is just '0')
            if len(segment) > 1 and segment[0] == '0':
                return False
            # 2. Must be between 0 and 255
            if int(segment) > 255:
                return False
            return True

        def helper(i, curr_ip, dots):
            # Base Case: Exactly 4 segments and we used the whole string
            if dots == 4 and i == len(s):
                res.append(curr_ip[:-1]) # Remove the trailing dot
                return
            
            # Pruning: If we have too many segments, stop
            if dots > 4:
                return 

            # The "Knife": An IP segment can only be 1, 2, or 3 digits long
            for j in range(1, 4):
                if i + j <= len(s):
                    segment = s[i:i+j]
                    
                    if isValid(segment):
                        # Explore: Move the start index to i+j, add segment, inc dots
                        helper(i + j, curr_ip + segment + '.', dots + 1)
        
        helper(0, "", 0)
        return res