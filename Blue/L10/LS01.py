INF = 10**9
def Bellman(src):
    distance[src] = 0
    for i in range(1, n):
        for j in range(m):
            u = graph[j][0]
            v = graph[j][1]
            w = graph[j][2]

            if distance[u] != INF and (distance[u] + w < distance[v]):
                distance[v] = distance[u] + w
                path[v] = u
    for k in range(m):
        u = graph[k][0]
        v = graph[k][1]
        w = graph[k][2]
        if distance[u] != INF and (distance[u] + w < distance[v]):
            return False
    return True

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = []
    path = [-1 for _ in range(n)]
    distance = [INF for _ in range(n)]

    for i in range(m):
        x, y, t = map(int, input().split())
        graph.append((x, y, t))
    res = Bellman(0)
    print("possible") if res == False else print ("not possible")
