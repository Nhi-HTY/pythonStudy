from heapq import heappush, heappop

def Dijkstra(s, e):
    INF = int(1e9) + 7
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

s = int(input())
for _ in range(s):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    cities = []
    for i in range(1, n+1):
        city = input()
        cities.append(city)
        p = int(input())
        for k in range(p):
            nr, cost = map(int, input().split())
            graph[i].append((nr, cost))
    q = int(input())
    for j in range(q):
        start, end = input().split()
        s = cities.index(start) + 1
        e = cities.index(end) + 1
        print(Dijkstra(s, e))
    input()