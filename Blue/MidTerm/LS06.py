import queue

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Cell:
    def __init__(self, r, c):
        self.r = r
        self.c = c

def isInMatrix(u, v, m, n):
    return 0 <= u < m and 0 <=v < n

def BFS(sr, sc):
    q = queue.Queue()
    q.put(Cell(sr, sc))
    dist[sr][sc] = 0
    visited[sr][sc] = True

    while q.qsize() > 0:
        u = q.get()
        for i in range(4):
            row = u.r + dx[i]
            column = u.c + dy[i]
            if isInMatrix(row, column, n, m) and listBomb[row][column] == False and visited[row][column] == False:
                q.put(Cell(row, column))
                dist[row][column] = dist[u.r][u.c] + 1
                visited[row][column] = True

while True:
    n, m = map(int, input().split())
    INF = 10**9
    if n == 0 and m == 0:
        break
    r = int(input())
    visited = [[False for i in range(m)] for j in range(n)]
    dist = [[INF for i in range(m)] for j in range(n)]
    listBomb = [[False for i in range(m)] for j in range(n)]
    for _ in range(r):
        bomb = list(map(int, input().split()))
        for i in range(bomb[1]):
            listBomb[bomb[0]][bomb[i+2]] = True
    sr, sc = map(int, input().split())
    dr, dc = map(int, input().split())
    BFS(sr, sc)
    print(dist[dr][dc])

