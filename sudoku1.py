board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
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
            if(valid(board, i, j, pa) == true):
                board[i][j] = pa
                solve_sudoku(board, ni, nj)
                board[i][j] = 0