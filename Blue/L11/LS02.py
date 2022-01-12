t = int(input())
INF = 10**9

def Floy():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

while True:
    n = int(input())
    if n == 0:
        break
    start, end = input().split()
    dist = [[INF] * n for i in range(n)]
    matrix = []
    for _ in range(n):
        type, direction, city1, city2, distance = input().split()
        m

