import queue
def BFS(s):
    count = 0
    visited = [False for i in range(n+1)]
    q = queue.Queue()
    q.put(s)
    visited[s] = True
    cat[s] = (1 if vertices[s-1] == 1 else 0)

    while q.qsize() > 0:
        u = q.get()
        for v in listNeighbor[u]:
            if not visited[v]:
                visited[v] = True

                if vertices[v-1] == 1:
                    cat[v] = cat[u] + 1

                if cat[v] <= m:
                    if len(listNeighbor[v]) == 1:
                        count += 1
                    else:
                        q.put(v)
    return count

n, m = map(int, input().split())
vertices = list(map(int, input().split()))
listNeighbor = [[] for i in range(n+1)]
cat = [0 for i in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    listNeighbor[u].append(v)
    listNeighbor[v].append(u)

count = BFS(1)
print(count)

