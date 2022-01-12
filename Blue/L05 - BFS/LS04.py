import queue

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
land = []

class Cell:
    def __init__(self, r, c):
        self.r = r
        self.c = c

def isInMaze(u, v, m, n):
    return 0 <= u < m and 0 <=v < n

def BFS(s):
    visited = [[False for i in range(w)] for j in range(h)]
    q = queue.Queue()
    visited[s.r][s.c] = True
    q.put(s)
    count = 1

    while q.qsize() > 0:
        u = q.get()
        for i in range(4):
            row = u.r + dx[i]
            column = u.c + dy[i]
            if isInMaze(row, column, h, w) and land[row][column] == "." and not visited[row][column]:
                q.put(Cell(row, column))
                visited[row][column] = True
                count += 1
    return count

for _ in range(t):
    land = []
    start = Cell(0, 0)
    w, h = map(int, input().split())
    for row in range(h):
        eachRow = input()
        for col in range(len(eachRow)):
            if eachRow[col] == "@":
                start = Cell(row, col)
        land.append(eachRow)
    print("Case {}: {}".format(_ + 1, BFS(start)))