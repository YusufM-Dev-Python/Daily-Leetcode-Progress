# Day 27 (Final Boss - Ultra Optimized): Sudoku Solver
# Topic: Backtracking with O(1) State Tracking (HashSets)
# Logic: Pre-calculate empty cells AND used numbers in rows/cols/boxes.

class Solution(object):
    def solveSudoku(self, board):
        # 1. State Tracking: Sets for O(1) average time complexity lookups
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # 2. Build the Initial State
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    empty_cells.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    # Mapping (r, c) to one of the nine 3x3 boxes (0-8)
                    box_id = (r // 3) * 3 + (c // 3)
                    boxes[box_id].add(val)

        def backtrack(idx):
            # Base Case: All empty cells filled successfully
            if idx == len(empty_cells):
                return True
            
            r, c = empty_cells[idx]
            box_id = (r // 3) * 3 + (c // 3)
            
            # Try numbers 1-9
            for char in "123456789":
                # O(1) Lookups! No more looping to check safety
                if char not in rows[r] and char not in cols[c] and char not in boxes[box_id]:
                    # CHOOSE: Place and update sets
                    board[r][c] = char
                    rows[r].add(char)
                    cols[c].add(char)
                    boxes[box_id].add(char)
                    
                    # EXPLORE
                    if backtrack(idx + 1):
                        return True
                    
                    # BACKTRACK: Undo placement and remove from sets
                    board[r][c] = "."
                    rows[r].remove(char)
                    cols[c].remove(char)
                    boxes[box_id].remove(char)
            
            return False

        backtrack(0)