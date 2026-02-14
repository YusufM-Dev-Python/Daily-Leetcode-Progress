# Day 10: Find All Anagrams in a String (LeetCode #438)
# Technique: Fixed-Size Sliding Window + Hash Map Comparison
# Time Complexity: O(n)
# Space Complexity: O(k)

class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        
        result = []
        k = len(p)
        p_count = {}
        win_count = {}

        # 1. INITIAL FILLING (The 'First Window')
        # We process the first 'k' characters of both strings to set up our comparison
        for i in range(k):
            p_count[p[i]] = p_count.get(p[i], 0) + 1
            win_count[s[i]] = win_count.get(s[i], 0) + 1

        # Check if the very first window is an anagram
        if p_count == win_count:
            result.append(0)

        # 2. SLIDING THE WINDOW
        # 'i' is the character entering the window
        # 'i-k' is the character leaving the window
        for i in range(k, len(s)):
            # Add new character (Coming into the window from the right)
            in_char = s[i]
            win_count[in_char] = win_count.get(in_char, 0) + 1

            # Remove old character (Falling out of the window from the left)
            out_char = s[i-k]
            win_count[out_char] -= 1

            # CRUCIAL: Why we use 'del'
            # Python dictionaries compare by keys AND values. 
            # If win_count has {'a': 0} and p_count doesn't have 'a', win_count == p_count will be FALSE.
            # We must delete the key entirely when the count hits zero to keep maps identical.
            if win_count[out_char] == 0:
                del win_count[out_char]

            # Check if current window matches
            if win_count == p_count:
                # The start index of the window is (current_index - window_size + 1)
                result.append(i - k + 1)
                
        return result