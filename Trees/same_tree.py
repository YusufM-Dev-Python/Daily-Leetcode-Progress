# Day 42: Same Tree (LeetCode #100)
# Folder: Trees
# Logic: Recursive Double-DFS. We compare two nodes at a time. 
# For two trees to be identical, every 'mirror' node must have the same value 
# and the same child structure.
# Time Complexity: O(min(N, M)) - where N and M are the number of nodes in both trees.
# Space Complexity: O(h) - recursion stack based on the height of the smaller tree.

class Solution(object):
    def isSameTree(self, p, q):
        # Base Case 1: If both territories are empty, they are the same.
        if not p and not q:
            return True

        # Base Case 2: Structural Mismatch. 
        # If one node exists but the other doesn't, the trees differ.
        if not p or not q:
            return False
            
        # Base Case 3: Value Mismatch.
        if p.val != q.val:
            return False

        # Recursive Step: The current nodes match! 
        # Now, send scouts to check if the left wings and right wings match.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)