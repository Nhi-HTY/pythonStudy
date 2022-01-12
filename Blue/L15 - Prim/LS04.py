import queue

class Node:
    def __init__(self, id = 0, dist = 0):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist <= other.dist

def prims(s):
    pq = queue.PriorityQueue()
    n = len(cityDict)
    visited = [False for i in range(n)]
    dist = [INF for i in range(n)]
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
    for i in range(n):
        if dist[i] >= INF:
            return "Impossible"
        ans += dist[i]
    return ans

t = int(input())
INF = 10**9
MAX = 50

for tc in range(t):
    input()
    m = int(input())
    id = 0
    graph = [[] for i in range(MAX*2)]
    cityDict = dict()
    for _ in range(m):
        city1, city2, distance = list(input().split())
        if city1 not in cityDict:
            cityDict[city1] = id
            id += 1
        if city2 not in cityDict:
            cityDict[city2] = id
            id += 1
        graph[cityDict[city1]].append(Node(cityDict[city2], int(distance)))
        graph[cityDict[city2]].append(Node(cityDict[city1], int(distance)))
    ans = prims(0)
    print("Case {}: {}".format(tc+1, ans))
