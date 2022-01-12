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
    n = int(input())
    r = int(input())
    graphS = [[] for _ in range(n)]
    graphE = [[] for _ in range(n)]
    distanceS = [INF] * (n+1)
    distanceE = [INF] * (n+1)
    for i in range(r):
        u, v = map(int, input().split())
        graphS[u].append((v, 1))
        graphS[v].append((u, 1))
        graphE[v].append((u, 1))
        graphE[u].append((v, 1))
    s, d = map(int, input().split())
    Dijkstra(s, graphS, distanceS)
    Dijkstra(d, graphE, distanceE)
    result = 0
    for j in range(n):
        result = max(result, distanceS[j] + distanceE[j])
    print("Case {}: {}".format(_+1, result))