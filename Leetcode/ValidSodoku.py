def createSubGrid(board):
    row3 = 0
    while row3 < 9:
        col3 = 0
        while col3 < 9:
            subGrid = []
            for i in range(row3, row3+3):
                for j in range(col3, col3+3):
                    if board[i][j] != ".":
                        subGrid.append(board[i][j])
            col3 += 3
        row3 += 3

matrix = []
i = 0
while i < 9:
    n = list(map(str, input().split()))
    matrix.append(n)
    i += 1

createSubGrid(matrix)