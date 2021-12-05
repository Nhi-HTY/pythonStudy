import sys
t = int(input())

sys.setrecursionlimit(10005)
def DFS(u):
    visited[u] = 1

    for v in graph[u]:
        if visited[v] == 1:
            return True
        elif visited[v] == 0:
            if DFS(v):
                return True

    visited[u] = 2
    return False

for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
    count = 0
    isLoop = False
    for j in range(n):
        if visited[j] == 0:
            isLoop = DFS(j)
            if isLoop:
                break
    print("YES") if isLoop == True else print("NO")

