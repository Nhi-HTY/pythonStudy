import queue
n = int(input())

def Dijkstra(src):
    distance[src] = 0
    pq = queue.PriorityQueue()
    pq.put((src, 0))

    while pq.qsize() > 0:
        u, dist = pq.get()

        for v, w in graph[u]:
            if w + dist < distance[v]:
                distance[v] = w + dist
                pq.put((v, distance[v]))

exit = int(input())
time = int(input())
m = int(input())
INF = int(1e9) + 7
distance = [INF] * 101
graph = [[] for _ in range(101)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[b].append((a, t))
Dijkstra(exit)
count = 0
for i in range(1, n+1):
    if distance[i] <= time:
        count += 1
print(count)

