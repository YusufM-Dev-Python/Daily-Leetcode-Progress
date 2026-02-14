# Day 40: Balanced Binary Tree (LeetCode #110)
# Logic: Bottom-Up DFS. We calculate height and check balance simultaneously.
# If any subtree is found unbalanced, we propagate '-1' all the way up 
# to avoid unnecessary calculations (Early Exit).
# Time Complexity: O(n) - Each node is visited once.
# Space Complexity: O(h) - Recursion stack depth equals tree height.

class Solution(object):
    def isBalanced(self, root):

        def dfs(node):
            # Base Case: An empty node is balanced and has height 0.
            if not node:
                return 0 

            # Step 1: Check the left wing. If it's already broken (-1), pass it up.
            left = dfs(node.left)
            if left == -1: return -1

            # Step 2: Check the right wing. If it's broken (-1), pass it up.
            right = dfs(node.right)
            if right == -1: return -1

            # Step 3: Compare heights. If the gap is > 1, this node is broken.
            if abs(left - right) > 1: 
                return -1

            # Step 4: If balanced, return the height to the parent node.
            return max(left, right) + 1
            
        # If the final result isn't -1, the entire tree is stable.
        return dfs(root) != -1