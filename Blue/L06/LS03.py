n, m, k = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * 51 for _ in range(51)]
table = []
lakes = []

def DFS(x, y):
    visited[x][y] = True
    isOcean = False
    temp = []
    s = []
    s.append((x, y))

    while len(s):
        r, c = s.pop()
        temp.append((r, c))

        if r == 0 or c == 0 or r == n - 1 or c == m - 1:
            isOcean = True

        for i in range(4):
            row = r + dx[i]
            column = c + dy[i]

            if row in range(n) and column in range(m) and matrix[row][column] == "." and not visited[row][column]:
                visited[row][column] = True
                s.append((row, column))
    if not isOcean:
        lakes.append(temp)

matrix = [None]*n
for i in range(n):
    matrix[i] = list(input())
for x in range(n):
    for y in range(m):
        if matrix[x][y] == "." and not visited[x][y]:
            DFS(x, y)

lakes.sort(key=lambda lake: len(lake))
sum_cell = 0

for i in range(len(lakes) - k):
    sum_cell += len(lakes[i])
    for r, c in lakes[i]:
        matrix[r][c] = '*'

print(sum_cell)

for m in range(n):
    print(''.join(matrix[m]))