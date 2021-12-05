import queue

total = int(input())
pq = queue.PriorityQueue()
queueRemove = queue.PriorityQueue()
for _ in range(total):
    eachLine = input()
    if eachLine[0] == "1":
        pq.put(int(eachLine.split()[1]))
    elif eachLine[0] == "2":
        value = eachLine.split()
        queueRemove.put(int(eachLine.split()[1]))
    else:
        while not queueRemove.empty() > 0 and queueRemove.queue[0] == pq.queue[0]:
            queueRemove.get()
            pq.get()
        print(pq.queue[0])