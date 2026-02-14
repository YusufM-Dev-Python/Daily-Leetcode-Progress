# Day 43: Symmetric Tree (LeetCode #101)
# Folder: Trees
# Logic: Mirror DFS. Unlike 'Same Tree', we compare the left child of 
# one node with the right child of the other to check for symmetry.
# Time Complexity: O(n) - Every node is visited once.
# Space Complexity: O(h) - Recursive stack space.

class Solution(object):
    def isSymmetric(self, root):
        if not root: 
            return True

        def dfs(left_node, right_node):
            # Base Case 1: Both are empty, still symmetric
            if not left_node and not right_node:
                return True
            
            # Base Case 2: One is empty or values don't match
            if not left_node or not right_node:
                return False
            
            if left_node.val != right_node.val:
                return False

            # The 'Mirror' Step: 
            # Compare Outer children (L.left, R.right) 
            # AND Inner children (L.right, R.left)
            return dfs(left_node.left, right_node.right) and \
                   dfs(left_node.right, right_node.left)
            
        return dfs(root.left, root.right)