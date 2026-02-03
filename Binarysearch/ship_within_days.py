class Solution(object):
    def shipWithinDays(self, weights, days):
        # The minimum capacity must be at least the heaviest package
        l = max(weights)
        # The maximum capacity would be shipping everything in one day
        r = sum(weights)

        while l <= r:
            mid = (l + r) // 2

            day_count = 1
            current_load = 0
            for w in weights:
                # If adding this package exceeds current capacity 'mid'
                if current_load + w > mid:
                    day_count += 1    # Send the ship, start a new day
                    current_load = w  # This package is the first for the next day
                else:
                    current_load += w
            
            if day_count > days:
                # We took too many days, we need more capacity
                l = mid + 1
            else:
                # We finished in time, try to find a smaller capacity
                r = mid - 1
                
        return l