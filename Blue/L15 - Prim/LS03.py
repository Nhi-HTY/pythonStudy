import queue

class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist <= other.dist

def prims(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    visited[s] = True
    dist[s] = 0

    while pq.qsize() > 0:
        u = pq.get().id
        visited[u] = True

        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
    ans = 0
    for i in range(n+1):
        if dist[i] < INF:
            ans += dist[i]
    return ans

t = int(input())
INF = 10**9

for tc in range(t):
    p = int(input())
    n = int(input())
    graph = [[] for i in range(n+1)]
    visited = [False for i in range(n+1)]
    dist = [INF for i in range(n+1)]
    m = int(input())
    for i in range(m):
        a, b, c = list(map(int, input().split()))
        graph[a].append(Node(b, c))
        graph[b].append(Node(a, c))
    ans = prims(1)
    print(ans*p)