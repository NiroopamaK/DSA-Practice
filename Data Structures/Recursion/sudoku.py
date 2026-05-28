# Sudoku Solver (Backtracking)

# Problem:
# Given a 9x9 Sudoku board, fill the empty cells (".")
# so that the board becomes valid.
#
# Rules:
# - Each row must contain digits 1–9 without repetition
# - Each column must contain digits 1–9 without repetition
# - Each 3x3 subgrid must contain digits 1–9 without repetition
#
# -------------------------------------------------------------
# Idea (Backtracking):
# - Try placing numbers 1–9 in empty cells
# - Check if placement is valid
# - Recursively solve the rest of the board
# - If stuck → backtrack (undo choice)
#
# -------------------------------------------------------------
# Time Complexity: O(9^(n*n)) worst case
# Space Complexity: O(1) (in-place)
# -------------------------------------------------------------


def solveSudoku(board):

    def isValid(r, c, val):
        # Check row
        for i in range(9):
            if board[r][i] == val:
                return False

        # Check column
        for i in range(9):
            if board[i][c] == val:
                return False

        # Check 3x3 box
        box_r = (r // 3) * 3
        box_c = (c // 3) * 3

        for i in range(3):
            for j in range(3):
                if board[box_r + i][box_c + j] == val:
                    return False

        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for n in map(str, range(1, 10)):
                        if isValid(r, c, n):
                            # ✅ FIX: assignment, not comparison
                            board[r][c] = n

                            if backtrack():
                                return True

                            # backtrack
                            board[r][c] = "."

                    return False  # no valid number found

        return True  # solved

    backtrack()


# Main function
def main():
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    solveSudoku(board)

    print("Solved Sudoku:")
    for row in board:
        print(row)


# -------------------------------------------------------------
if __name__ == "__main__":
    main()