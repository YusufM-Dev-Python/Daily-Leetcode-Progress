# Day 7: Majority Element (LeetCode #169)
# Algorithm: Boyer-Moore Voting Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1) using this algo

class Solution(object):
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for i in nums:
            # When count reaches 0, the previous 'army' is neutralized.
            # We pick the current element as the new candidate (The King).
            if count == 0:
                candidate = i
                count = 1
            
            # If the current element is the same as the candidate,
            # the King's army grows (The Reinforcement).
            elif i == candidate:
                count += 1
            
            # If the current element is different, it 'kills' one soldier 
            # from the King's army (The Assassination).
            else: 
                count -= 1
                
        # The Majority Element is guaranteed to appear more than n/2 times,
        # so it will always be the last candidate standing.
        return candidate