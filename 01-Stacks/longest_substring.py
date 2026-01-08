# Day 11: Longest Substring Without Repeating Characters (LeetCode #3)
# Technique: Dynamic Sliding Window + Hash Set
# Time Complexity: O(n)
# Space Complexity: O(min(m, n)) where m is the size of the charset

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = 0
        l = 0
        # A set is used for O(1) average time complexity lookups
        char_set = set()

        for right in range(len(s)):
            # If we find a duplicate, we shrink the window from the LEFT
            # until the duplicate character is removed from the set.
            while s[right] in char_set:
                char_set.remove(s[l])
                l += 1
            
            # Add the current character and update the maximum length
            char_set.add(s[right])
            
            # Window length is (right - left + 1)
            res = max(res, right - l + 1)
            
        return res