# Day 12: Contiguous Array (LeetCode #525)
# Topic: Hash Map + Prefix Sum (Balance Score)
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def findMaxLength(self, nums):
        # We start with score 0 at index -1 to handle subarrays 
        # that start from the very beginning (index 0).
        mappi = {0: -1}
        score = 0
        max_len = 0

        for i in range(len(nums)):
            # "The Score": Balance 0s and 1s
            if nums[i] == 0:
                score -= 1
            else:
                score += 1
            
            # If the same score is seen again, it means between the 
            # previous index and now, the net change was ZERO.
            # (Meaning equal number of 0s and 1s were added).
            if score in mappi:
                dist = i - mappi[score]
                max_len = max(max_len, dist)
            else:
                # We only store the FIRST time a score is seen 
                # to maximize the distance (longest chain).
                mappi[score] = i
                
        return max_len