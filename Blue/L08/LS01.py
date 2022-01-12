import queue
INF = int(1e9) + 7
distance = [INF] * 505
def Dijkstra(src):
    pq = queue.PriorityQueue()
    distance[src] = 0
    pq.put((src, 0))

    while not pq.empty():
        u, dist = pq.get()
        for v, w in graph[u]:
            if w + dist < distance[v]:
                distance[v] = w + dist
                pq.put((v, distance[v]))

n = int(input())
graph = [[] for _ in range(505)]
for _ in range(n):
    vertex = list(map(int, input().split()))
    graph[vertex[0]].append((vertex[1], vertex[2]))
    graph[vertex[1]].append((vertex[0], vertex[2]))
u = int(input())
Dijkstra(u)
q = int(input())
for i in range(q):
    v = int(input())
    if distance[v] != INF:
        print(distance[v])
    else:
        print("NO PATH")
