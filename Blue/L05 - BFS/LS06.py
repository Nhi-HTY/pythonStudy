import queue

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
land = []

class Cell:
    def __init__(self, r, c):
        self.r = r
        self.c = c

def isInMatrix(u, v, m, n):
    return 0 <= u < m and 0 <= v < n

def BFS(row, col):
    q = queue.Queue()
    q.put(Cell(row, col))
    count = 1
    matrix[row][col] = 0

    while q.qsize() > 0:
        u = q.get()
        for i in range(4):
            row = u.r + dx[i]
            column = u.c + dy[i]
            if isInMatrix(row, column, n, m) and matrix[row][column] == 1:
                q.put(Cell(row, column))
                matrix[row][column] = 0
                count += 1
    listSlick[count] += 1

while True:
    matrix = []
    listSlick = [0] * (1000 * 1000)
    n, m = map(int, input().split())
    totalSlick = 0
    if n == 0 and m == 0:
        break
    for _ in range(n):
        eachRow = list(map(int, input().split()))
        matrix.append(eachRow)
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 1:
                totalSlick += 1
                BFS(row, col)
    print(totalSlick)

    for i in range(1, n * m  + 1):
            if listSlick[i]:
                print(i, listSlick[i], sep=' ')


