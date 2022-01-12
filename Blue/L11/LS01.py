t = int(input())
INF = 10**9

def Floy():
    for k in range(M):
        for i in range(M):
            for j in range(M):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

test = 0
while test < t:
    line = input()
    matrix = []
    M = len(line)
    dist = [[INF] * M for i in range(M)]
    for i in range(M):
        if i == 0:
            matrix.append(line)
        else:
            line = input()
            matrix.append(line)
        for j in range(M):
            if matrix[i][j] == "Y":
                dist[i][j] = 1
            elif i == j:
                dist[i][j] = 0

    Floy()
    friend, index = 0, 0

    for i in range(M):
        count = 0
        for j in range(M):
            if dist[i][j] == 2:
                count += 1
        if count > friend:
            friend = count
            index = i
    print(index, friend)
    test += 1
