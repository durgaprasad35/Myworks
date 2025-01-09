def is_safe(board,row,col,n):
    for i in range(row):
        if board[i][col] ==1:
            return False 
    for i,j in zip(range(row,-1,-1) ,range(col,-1,-1)):
            if board[i][j]==1:
                return False 
    for i,j in zip(range(row,-1,-1),range(col,n)):
            if board[i][j]==1:
                return False 
    return True
def solve_nqueens_util(board,row,n,solutions):
    if row>=n:
        solutions.append(["".join("Q" if col==1 else "." for col in board[row]) for row in range(n)]) 
        return 
    for col in range(n):
        if is_safe(board,row,col,n):
            board[row][col] = 1 
            solve_nqueens_util(board,row+1,n,solutions) 
            board[row][col] = 0 
def solve_nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)] 
    solutions = [] 
    solve_nqueens_util(board,0,n,solutions) 
    return solutions 
n=4
solutions = solve_nqueens(n) 
for e in solutions:
    print(e)