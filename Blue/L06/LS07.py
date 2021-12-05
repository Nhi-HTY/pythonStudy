h, w = map(int, input().split())
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1 , 0, -1]

def DFS(row, col):
    path = 1
    s = []
    s.append((row, col))
    curOrd = ord(listLetter[row][col])

    while len(s) > 0:
        r, c = s.pop()

        for i in range(8):
            x = r + dx[i]
            y = c + dy[i]

            if x in range(h) and y in range(w) and ord(listLetter[x][y]) == curOrd + 1:
                longestPath = max(longestPath, DFS(x, y))
                curOrd += 1
                path
                s.append((x, y))
                break
    return path

case = 1
while True:
    longestPath = 0
    listLetter = [[]] * h
    for i in range(h):
        listLetter[i] = list(input())
    for row in range(h):
        for col in range(w):
            if listLetter[row][col] == "A":
                path = DFS(row, col)
                longestPath = max(path, longestPath)
    print("Case {}: {}". format(case, longestPath))
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    case += 1
