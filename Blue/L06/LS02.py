t = int(input())

def DFS(scr):
    s = [scr]
    visited[scr] = True

    while len(s):
        u = s.pop()

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                s.append(v)

for _ in range(t):
    n = int(input())
    e = int(input())
    graph = [[] for i in range(n)]
    visited = [False for i in range(n)]
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    count = 0
    for j in range(n):
        if not visited[j]:
            count += 1
            DFS(j)
    print(count)