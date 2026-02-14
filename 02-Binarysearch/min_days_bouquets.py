class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1
            
        l = 1
        r = max(bloomDay)
        
        while l <= r:
            mid = (l + r) // 2
            formed = 0
            adjacent = 0
            
            for b in bloomDay:
                if b <= mid:
                    adjacent += 1
                    if adjacent == k:
                        formed += 1
                        adjacent = 0
                else:
                    adjacent = 0
            
            if formed >= m:
                r = mid - 1
            else:
                l = mid + 1
                
        return l