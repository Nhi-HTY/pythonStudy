from heapq import heappush, heappop

INF = int(1e9) + 7
def Dijkstra(s):
    distance = [INF] * (n+1)
    distance[s] = 0
    pq = [(0, s)]

    while pq:
        dist, u = heappop(pq)
        if dist > distance[u]:
            continue
        for v, w in graph[u]:
            if w + dist < distance[v]:
                distance[v] = w + dist
                heappush(pq, (distance[v], v))
    return distance

n, m, k, x = map(int, input().split())
cities = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))
a, b = map(int, input().split())
timeA = Dijkstra(a)
timeB = Dijkstra(b)
result = INF
for city in cities:
    if timeB[city] <= x:
        result = min(result, timeA[city] + timeB[city])
print(result) if result < INF else print(-1)