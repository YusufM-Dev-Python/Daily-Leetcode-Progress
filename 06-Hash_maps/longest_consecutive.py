# Day 8: Longest Consecutive Sequence (LeetCode #128)
# Topic: Hash Sets & Intelligent Sequences
# Time Complexity: O(n) 
# Space Complexity: O(n)

class Solution(object):
    def longestConsecutive(self, nums):
        # We use a Hash Set for O(1) lookups instead of sorting
        my_set = set(nums)
        streak = 0
        longest = 0

        for i in my_set:
            # CRUCIAL: Only start building a sequence if 'i' is the START
            # If (i-1) is in the set, then 'i' is already part of a sequence
            if (i - 1) not in my_set:
                num = i
                streak = 1

                # Check for consecutive numbers forward
                while (num + 1) in my_set:
                    num += 1
                    streak += 1
            
            longest = max(longest, streak)

        return longest