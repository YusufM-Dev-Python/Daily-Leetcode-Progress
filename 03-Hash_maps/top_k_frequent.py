# Day 9: Top K Frequent Elements (LeetCode #347)
# Topic: Hash Maps & Sorting with Lambda
# Time Complexity: O(n log n) due to sorting

class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}

        # Step 1: Count frequencies using a Hash Map
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        # Step 2: Convert dictionary to a list of tuples and sort
        # .items() converts {1: 3, 2: 2} into [(1, 3), (2, 2)]
        # lambda x: x[1] tells Python to sort based on the frequency (the value)
        # reverse = True ensures we get the highest frequencies first
        pairs = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        result = []
        # Step 3: Extract the first k elements
        for i in range(k):
            # pairs[i] is a tuple (element, frequency)
            # pairs[i][0] gets the element itself
            result.append(pairs[i][0])
            
        return result