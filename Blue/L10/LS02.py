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

    for k in range(n):
        for e in graph:
            u, v, w = e[0], e[1], e[2]
            if distance[u] != INF and distance[u] + w < distance[v]:
                distance[v] = -INF

t = int(input())

for _ in range(t):
    input()
    n = int(input())
    busyness = list(map(int, input().split()))
    m = int(input())
    graph = []
    for i in range(m):
        source, dest = map(int, input().split())
        graph.append((source, dest, (busyness[dest-1] - busyness[source-1])**3))
    path = [-1 for _ in range(n+1)]
    distance = [INF for _ in range(n+1)]
    Bellman(1)
    print("Case {}:".format(_+1))
    q = int(input())
    for x in range(q):
        query = int(input())
        print(distance[query]) if distance[query] != INF and distance[query] >= 3 else print("?")

