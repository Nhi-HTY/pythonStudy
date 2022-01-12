from heapq import heappush, heappop
INF = int(1e9) + 7
def Dijkstra(src, graph, distance):
    distance[src] = 0
    pq = [(0, src)]

    while pq:
        dist, u = heappop(pq)

        for v, w in graph[u]:
            if w + dist < distance[v]:
                distance[v] = w + dist
                heappush(pq, (distance[v], v))

t = int(input())
for _ in range(t):
    n, m, k, s, e = map(int, input().split())
    graphS = [[] for _ in range(n+1)]
    graphE = [[] for _ in range(n+1)]
    distanceS = [INF] * (n+1)
    distanceE = [INF] * (n+1)
    pq = []
    for i in range(m):
        d, c, l = map(int, input().split())
        graphS[d].append((c, l ))
        graphE[c].append((d, l))
    Dijkstra(s, graphS, distanceS)
    Dijkstra(e, graphE, distanceE)
    for j in range(k):
        u, v, j = map(int, input().split())
        a = distanceS[u] + j + distanceE[v]
        b = distanceS[v] + j + distanceE[u]
        heappush(pq, min(a, b))
    result = heappop(pq)
    print(result) if result < INF else print(-1)