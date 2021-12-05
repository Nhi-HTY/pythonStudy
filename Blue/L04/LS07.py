import queue

n, b = map(int, input().split())
q = queue.Queue()
end = 0

for _ in range(n):
    t, d = map(int, input().split())
    while q.qsize() > 0 and t >= q.queue[0]:
        q.get()

    if q.qsize() <= b:
        end = max(end, t) + d
        q.put(end)
        print(end, end = " ")
    else:
        print(-1, end =" ")