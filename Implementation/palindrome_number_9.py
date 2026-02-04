class Solution(object):
    def isPalindrome(self, x):
        # Edge cases: 
        # 1. Negative numbers are never palindromes (the '-' sign)
        # 2. Numbers ending in 0 (except 0 itself) can't be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverse = 0
        # Optimization: Only reverse half of the number
        # When x <= reverse, we've reached the middle
        while x > reverse:
            reverse = (reverse * 10) + (x % 10)
            x = x // 10
            
        # For even length numbers: x should equal reverse (e.g., 12|21 -> 12 == 12)
        # For odd length numbers: x should equal reverse // 10 (e.g., 12|3|21 -> 12 == 123//10)
        return x == reverse or x == reverse // 10