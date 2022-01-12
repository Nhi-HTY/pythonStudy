import queue

def BFS(k, listKey):
    dist = [-1] * 100000
    q = queue.Queue()
    q.put(k)
    dist[k] = 0

    while q.qsize() > 0:
        u = q.get()

        for key in listKey:
            v = u*key%100000

            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.put(v)

                if v == lockKey:
                    return dist[v]
    return -1

key, lockKey = map(int, input().split())
n = int(input())
listKey = list(map(int, input().split()))
print(BFS(key, listKey))