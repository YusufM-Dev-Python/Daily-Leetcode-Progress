"""
Day 44: Path Sum (LeetCode #112)
Problem Link: https://leetcode.com/problems/path-sum/

Logic: 
This is a Top-Down DFS approach. We 'carry' the remaining sum needed as we 
traverse deeper into the tree. By subtracting the current node's value at 
each step, the problem simplifies to: "Is there a leaf node whose value 
equals the remaining sum?"

Complexity Analysis:
- Time: O(N) where N is the number of nodes (we visit each node once).
- Space: O(H) where H is the height of the tree (due to recursion stack).
"""

class Solution(object):
    def hasPathSum(self, root, targetSum):
        # Base Case 1: If the tree is empty, no path can exist.
        if not root:
            return False

        # Base Case 2: We've reached a LEAF node (no children).
        # Check if the value of this leaf is exactly what we need.
        if not root.left and not root.right:
            return targetSum == root.val

        # Recursive Step:
        # Subtract the current node's value from our target.
        rem_sum = targetSum - root.val
        
        # If either the left subtree OR the right subtree has a path 
        # that satisfies the remaining sum, return True.
        return self.hasPathSum(root.left, rem_sum) or \
               self.hasPathSum(root.right, rem_sum)