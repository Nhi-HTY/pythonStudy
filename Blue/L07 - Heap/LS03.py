import queue
n = int(input())

while True:
    if n == 0:
        break
    cost = 0
    pq = queue.PriorityQueue()
    listNum = list(map(int, input().split()))
    for i in range(n):
        pq.put(listNum[i])
    while pq.qsize() > 1:
        first = pq.get()
        second = pq.get()
        total = first + second
        pq.put(total)
        cost += total
    print(cost)
    n = int(input())


