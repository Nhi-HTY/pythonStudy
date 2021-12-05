import queue

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
totalSheep = totalWolf = 0

def BFS(row, col):
    global totalSheep, totalWolf
    q = queue.Queue()
    q.put((row, col))
    canEscape = False
    sheep = (1 if land[row][col] == "k" else 0)
    wolf = (1 if land[row][col] == "v" else 0)
    land[row][col] = "#"

    while q.qsize() > 0:
        r, c = q.get()
        for i in range(4):
            x = r + dx[i]
            y = c + dy[i]

            if not (x in range(n) and y in range(m)):
                canEscape = True
                continue

            if land[x][y] != "#":
                sheep += (1 if land[x][y] == "k" else 0)
                wolf += (1 if land[x][y] == "v" else 0)
                land[x][y] = "#"
                q.put((x, y))

    if canEscape:
        totalSheep += sheep
        totalWolf += wolf
    else:
        if sheep > wolf:
            totalSheep += sheep
        else:
            totalWolf += wolf


n, m = map(int, input().split())
land = [None] * 1000
for i in range(n):
    land[i] = list(input())
for row in range(n):
    for col in range(m):
        if land[row][col] != "#":
            BFS(row, col)

print(totalSheep, totalWolf)