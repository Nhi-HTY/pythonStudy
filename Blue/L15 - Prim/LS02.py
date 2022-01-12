import math
import queue

class Node:
    def __init__(self, id = 0, dist = 0):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist <= other.dist

def prims(graph, s):
    n = len((graph))
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    visited = [False for i in range(n)]
    dist = [1e9] * n
    dist[s] = 0
    cost = 0

    while pq.qsize() > 0:
        u = pq.get().id
        visited[u] = True

        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
    for i in range(n):
        cost += dist[i]
    return cost

def distance(x1, y1, x2, y2):
    square_dis = (x1-x2)**2 + (y1-y2)**2
    return math.sqrt(square_dis)

while True:
    try:
        n = int(input())
        x = [0] * n
        y = [0] * n
        for i in range(n):
            x[i], y[i] = map(int, input().split())
        graph = []
        for i in range(n):
            graph.append([])
            for j in range(n):
                graph[i].append(Node(j, distance(x[i], y[i], x[j], y[j])))
        m = int(input())
        for i in range(m):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            graph[u][v].dist = 0
            graph[v][u].dist = 0
        ans = prims(graph, 0)
        print("%.2f" % ans)
    except EOFError:
        exit()
