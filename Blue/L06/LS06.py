import sys
sys.setrecursionlimit(100000)

t = int(input())
dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, 0, 1, -1, 0, 1, -1]

def DFS(row, col, quoteIndex):
    global exist
    if quoteIndex == len(quote):
        exist = True
        return

    for i in range(8):
        vr = row + dx[i]
        vc = col + dy[i]

        if (vr in range(r) and vc in range(c)) and visited[vr][vc] == False and matrix[vr][vc] == quote[quoteIndex]:
            visited[vr][vc] = True
            DFS(vr, vc, quoteIndex + 1)
            visited[vr][vc] = False


for _ in range(t):
    r, c = map(int, input().split())
    matrix = [[] for i in range(c) for j in range(r)]
    visited = [[False for i in range(c)] for j in range(r)]
    quote = "ALLIZZWELL"
    for k in range(r):
        matrix[k] = list(input())

    exist = False

    for row in range(r):
        for col in range(c):
            if matrix[row][col] == "A" and not exist:
                DFS(row, col, 1)

    print("YES") if exist else print("NO")
    input()
