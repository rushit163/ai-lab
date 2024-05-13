def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, row, n):
    if row >= n:
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = 0

    return False
def print_solution(board):
    for row in board:
        print(' '.join(map(str, row)))
n = int(input("Enter the value of N for N-Queens problem: "))
board = [[0 for _ in range(n)] for _ in range(n)]
if solve_n_queens(board, 0, n):
    print("Solution exists:")
    print_solution(board)
else:
    print("No solution exists for this configuration.")