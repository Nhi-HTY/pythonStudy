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
                path[v] = u

def MST():
    ans = 0
    for i in range(n+1):
        if path[i] != -1:
            ans += dist[i]
    print(ans)

n, m = map(int, input().split())
INF = 10**9

visited = [False for i in range(n+1)]
path = [-1 for i in range(n+1)]
dist = [INF for i in range(n+1)]
graph = [[] for i in range(n+1)]
for _ in range(m):
    x, y, r = list(map(int, input().split()))
    graph[x].append(Node(y, r))
    graph[y].append(Node(x, r))
s = int(input())
prims(s)
MST()
