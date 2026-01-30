class Solution(object):
    def minEatingSpeed(self, piles, h):
        # The range of possible speeds K:
        # Minimum speed is 1, Maximum is the biggest pile
        l = 1        
        r = max(piles)
        
        while l <= r:
            mid = (l + r) // 2 # Current speed we are testing
            total_hours = 0
            
            # Calculate how many hours it takes to eat all piles at speed 'mid'
            for pile in piles:
                # This is a clever way to do math.ceil(pile / mid) without floats
                total_hours += (pile + mid - 1) // mid
            
            if total_hours > h:
                # Too slow! We need to increase the speed
                l = mid + 1
            else:
                # We can finish on time, but can we do it even slower?
                # Move 'r' to check smaller speeds
                r = mid - 1
                
        # 'l' will settle on the minimum speed required to finish within h hours
        return l