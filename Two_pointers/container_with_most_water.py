# Day 30: Container With Most Water (LeetCode #11)
# Milestone: 1 MONTH COMPLETED! 🏆
# Technique: Two-Pointer (Greedy Approach)
# Complexity: O(n) Time, O(1) Space

class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        max_area = 0
        
        while l < r:
            # 1. Calculate the current dimensions
            # Width is the distance between pointers
            w = r - l
            # Height is limited by the shorter bar (it would overflow otherwise)
            h = min(height[l], height[r])
            
            # 2. Update the global maximum
            area = w * h 
            max_area = max(max_area, area)
            
            # 3. THE GREEDY MOVE:
            # To find a bigger area, we need a taller bar.
            # We move the pointer that points to the SHORTER bar 
            # because it's the bottleneck.
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_area