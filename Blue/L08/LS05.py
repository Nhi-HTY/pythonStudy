from heapq import heappush, heappop

INF = int(1e9) + 7
def Dijkstra(s, e):
    distance = [INF] * (n+1)
    distance[s] = 0
    pq = [(0, s)]

    while pq:
        dist, u = heappop(pq)

        if u == e:
            break

        for v, w in graph[u]:
            if w + dist < distance[v]:
                distance[v] = w + dist
                heappush(pq, (distance[v], v))
    return distance[e]

t = int(input())
for _ in range(t):
    n, m, s, e = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    result = Dijkstra(s, e)
    print("Case #{}: {}".format(_+1, result)) if result < INF else print("Case #{}: unreachable".format(_+1))