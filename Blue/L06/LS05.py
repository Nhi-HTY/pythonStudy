def DFS(u):
    s = []
    s.append(u)
    impact = 1
    visited[u] = True

    while len(s) > 0:
        u = s.pop()
        for v in graph[u]:
            if visited[v] == False:
                impact += 1
                visited[v] = True
                s.append(v)
    return impact

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
maxImpact = 1
for j in range(1, n+1):
    visited = [False] * (n + 1)
    impact = DFS(j)
    maxImpact = max(maxImpact, impact)
print(maxImpact)

