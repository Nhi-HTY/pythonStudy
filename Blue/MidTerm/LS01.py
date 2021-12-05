import queue
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    priorityList = list(map(int, input().split()))
    q = queue.Queue()
    for i in range(n):
        q.put((priorityList[i], i))
    sortedPriorityList = priorityList
    sortedPriorityList.sort()
    minutes = 0
    index = n-1
    while True:
        value, position = q.get()
        if value < sortedPriorityList[index]:
            q.put((value, position))
        elif value == sortedPriorityList[index] and position != m:
            minutes += 1
            sortedPriorityList.pop()
            index -= 1
        elif value == sortedPriorityList[index] and position == m:
            minutes += 1
            print(minutes)
            break

