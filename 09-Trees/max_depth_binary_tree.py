# Day 40: Maximum Depth of Binary Tree (LeetCode #104)
# Logic: Recursive DFS. We traverse down to the leaves. 
# Each node waits for its left and right children to report their depths, 
# then picks the 'winner' (max) and adds 1 (itself) to pass back up.
# Time Complexity: O(n) - We visit every node exactly once.
# Space Complexity: O(h) - Where h is the height of the tree (stack space for recursion).

class Solution(object):
    def maxDepth(self, root):
        # Base Case: If the node is empty (The Void), it has 0 depth.
        if not root:
            return 0

        else:
            # Step 1: Scout the depth of the left wing.
            l_depth = self.maxDepth(root.left)
            
            # Step 2: Scout the depth of the right wing.
            r_depth = self.maxDepth(root.right)
            
            # Step 3: The current node adds itself (+1) to the 
            # maximum depth found among its children.
            return (max(l_depth, r_depth) + 1)