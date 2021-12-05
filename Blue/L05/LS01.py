import queue

def BFS(s, adjacencyList, visited, path):
    queueVertices = queue.Queue()
    visited[s] = True
    queueVertices.put(s)
    path[s] = 0
    while queueVertices.qsize() > 0:
        vertice = queueVertices.get()
        for x in adjacencyList[vertice]:
            if not visited[x]:
                visited[x] = True
                queueVertices.put(x)
                path[x] = path[vertice] + 1
    return path

def printBFS(s, n, path):
    for i in range(1, n+1):
        if i != s:
            if path[i] == -1:
                print(-1, end = " ")
            else:
                print(path[i]*6, end =" ")
    print()

queries = int(input())
for i in range(queries):
    n, m = map(int, input().split())
    adjacencyList = [[] for vertices in range(n+1)]
    visited = [False for i in range(n+1)]
    path = [-1 for i in range(n+1)]
    for j in range(m):
        u, v = map(int, input().split())
        adjacencyList[u].append(v)
        adjacencyList[v].append(u)
    s = int(input())
    path = BFS(s, adjacencyList, visited, path)
    printBFS(s, n, path)