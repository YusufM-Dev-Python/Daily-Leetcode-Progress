# Day 22: Word Search
# Topic: 2D Grid Backtracking (DFS)
# Logic: Explore 4 directions and use a temporary marker to avoid reuse.

class Solution(object):
    def exist(self, board, word):
        def helper(r, c, idx):
            # 1. Base Case: If index matches word length, we found it!
            if idx == len(word):
                return True
            
            # 2. Boundary & Character Check:
            # Out of bounds OR current cell doesn't match the word's character
            if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or
                board[r][c] != word[idx]):
                return False
            
            # 3. Action: "Mark" the cell as visited using a placeholder
            # This prevents the recursion from using the same letter twice in one path.
            temp = board[r][c]
            board[r][c] = '#'

            # 4. Explore: Try all 4 adjacent directions (Down, Up, Right, Left)
            # If ANY direction returns True, the whole thing is True.
            res = (helper(r + 1, c, idx + 1) or 
                   helper(r - 1, c, idx + 1) or
                   helper(r, c + 1, idx + 1) or 
                   helper(r, c - 1, idx + 1))

            # 5. Backtrack: Restore the cell for other starting points/paths
            board[r][c] = temp
            return res
        
        # Main: Try starting the search from every single cell in the grid
        for r in range(len(board)):
            for c in range(len(board[0])):
                # Optimization: Only start helper if the first letter matches
                if board[r][c] == word[0] and helper(r, c, 0):
                    return True
        return False