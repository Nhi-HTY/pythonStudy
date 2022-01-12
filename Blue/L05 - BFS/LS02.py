import queue

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maze = []

class Cell:
    def __init__(self, r, c):
        self.r = r
        self.c = c

def isInMaze(u, v, m, n):
    return 0 <= u < m and 0 <=v < n

def BFS(s, e):
    visited = [[False for i in range(n)] for j in range(m)]
    q = queue.Queue()
    visited[s.r][s.c] = True
    q.put(s)

    while q.qsize() > 0:
        u = q.get()
        if u.r == e.r and u.c == e.c:
            return True
        for i in range(4):
            row = u.r + dx[i]
            column = u.c + dy[i]
            if isInMaze(row, column, m, n) and maze[row][column] == "." and not visited[row][column]:
                q.put(Cell(row, column))
                visited[row][column] = True
    return False

for _ in range(t):
    maze = []
    m, n = map(int, input().split())
    for row in range(m):
        eachRow = input()
        maze.append(eachRow)
    entries = []
    for x in range(m):
        for y in range(n):
            if maze[x][y] == "." and ((x == 0 or x == m - 1) or (y == 0 or y == n - 1)):
                entries.append(Cell(x, y))
    if len(entries) != 2:
        print("invalid")
    else:
        print("valid" if BFS(entries[0], entries[1]) else "invalid")