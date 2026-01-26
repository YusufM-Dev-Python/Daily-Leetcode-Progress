# Day 29 (Part 2): Two Sum II - Sorted Array
# Technique: Collision Pointers (Left and Right meeting in the middle)
# Complexity: O(n) Time, O(1) Space

class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1

        while l < r:
            current_sum = numbers[l] + numbers[r]
            
            if current_sum == target:
                # The problem asks for 1-based indexing
                return [l + 1, r + 1]
            
            elif current_sum > target:
                # Sum is too big, move the right pointer left to decrease it
                r -= 1
            
            else:
                # Sum is too small, move the left pointer right to increase it
                l += 1
        
        return []