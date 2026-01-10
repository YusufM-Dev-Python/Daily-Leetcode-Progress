# Day 6: Group Anagrams (LeetCode #49)
# Topic: Hash Maps & Sorting
# Time Complexity: O(n * k log k) where n is number of strings and k is max length of a string

class Solution(object):
    def groupAnagrams(self, strs):
        # We use a dictionary to group words that share the same sorted 'key'
        group = {}

        for word in strs:
            # 1. CRUCIAL: Sort the word and convert to a tuple
            # Anagrams like "eat" and "tea" both become ('a', 'e', 't') when sorted
            key = tuple(sorted(word))
            
            if key in group:
                group[key].append(word)     
            else:
                group[key] = [word]
        
        # 2. RETURN: group.values() returns the lists of grouped anagrams
        return list(group.values())