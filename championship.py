board = [
    [0,0,0,0,0,4,0,0,7],
    [0,2,0,0,1,0,9,5,0],
    [6,0,0,2,0,0,0,0,0],
    [0,0,6,8,0,0,0,1,0],
    [0,5,0,1,0,0,4,0,8],
    [2,0,0,0,0,0,6,0,0],
    [0,0,0,0,7,0,0,0,0],
    [1,8,0,0,0,0,0,0,0],
    [0,0,4,0,6,0,0,9,0]
]

def print_board(board):
    for i in range(0,9):
        for j in range(0,9):
            print(board[i][j]," ",end="")
            if((j+1) % 3 == 0 and j != 8):
                print(" | ",end="")
        print(" ")
        if((i+1)%3 == 0 and i != 8):
            print("---------------------------------")

def solve_sudoku(board, i, j): 
    if(i == len(board)):
        print_board(board)
        return
    ni = 0 
    nj = 0
    if(j == len(board[0]) - 1):
        ni = i + 1
        nj = 0
    else:
        ni = i
        nj = j + 1 
    if(board[i][j] != 0):
        solve_sudoku(board, ni, nj)
    else:
        for pa in range(1,10):
            if(valid(board, i, j, pa) == True):
                board[i][j] = pa
                solve_sudoku(board, ni, nj)
                board[i][j] = 0

def valid(board, x, y, answer):

    for j in range(0,len(board[0])):
        if(board[x][j] == answer):
            return False
    for i in range(0,len(board)):
        if(board[i][y] == answer):
            return False


    ci = x // 3 * 3
    cj = y // 3 * 3
    for i in range(0,3):
        for j in range(0,3):
            if(board[ci + 1][cj + j] == answer):
                return False
    return True

print("Original Sudoku Board: ")
print("\n")
print_board(board)
print("\n\nSolved Sudoku Board: ")
print("\n")
solve_sudoku(board, 0, 0)
