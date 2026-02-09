# Day 41: Diameter of Binary Tree (LeetCode #543)
# Folder: Trees
# Logic: Post-Order DFS. Each node calculates the height of its children.
# The 'Diameter' at any node is left_height + right_height.
# We update the global maximum 'ans' while returning the height to the parent.
# Time Complexity: O(n) - We visit each node once.
# Space Complexity: O(h) - Recursive stack space based on tree height.

class Solution(object):
    def diameterOfBinaryTree(self, root):
        # self.ans acts as the 'Global Record Holder' for the longest path seen.
        self.ans = 0

        def dfs(node):
            # Base Case: If we hit a Void, height is 0.
            if not node: 
                return 0

            # Step 1: Scout the max height of the left and right territories.
            left_h = dfs(node.left)
            right_h = dfs(node.right)

            # Step 2: The 'Diameter' through THIS node is the sum of both heights.
            # We check if this beats the current Global Record.
            self.ans = max(self.ans, left_h + right_h)

            # Step 3: Return the height of this subtree to the parent.
            # Height is the tallest child + 1 (representing the current node).
            return (max(left_h, right_h) + 1)
            
        dfs(root)
        return self.ans