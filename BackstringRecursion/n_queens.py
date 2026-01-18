# Day 21: N-Queens (The Hard Boss)
# Topic: 2D Backtracking & Constraint Satisfaction
# Logic: Place one queen per row and check 3 directions for safety.

class Solution(object):
    def solveNQueens(self, n):
        # 1. Initialize empty board
        board = [["."]*n for _ in range(n)]
        res = []

        def safety(r, c):
            # Check Vertical (Above)
            for i in range(r):
                if board[i][c] == "Q": return False
            
            # Check Upper-Left Diagonal
            i, j = r, c
            while i >= 0 and j >= 0:
                if board[i][j] == "Q": return False
                i -= 1; j -= 1
            
            # Check Upper-Right Diagonal
            i, j = r, c
            while i >= 0 and j < n:
                if board[i][j] == 'Q': return False
                i -= 1; j += 1
                
            return True

        def helper(row):
            # Base Case: All queens placed
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if safety(row, col):
                    # Choose
                    board[row][col] = 'Q'
                    # Explore next row
                    helper(row + 1)
                    # Backtrack (Undo)
                    board[row][col] = "."

        helper(0)
        return res