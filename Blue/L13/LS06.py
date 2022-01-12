import queue
n = int(input())
listPrice = queue.PriorityQueue()
listYear = list(map(int, input().split()))
i = 0
for year in listYear:
    buy = year
    for j in range(i+1, n):
        if listYear[j] != buy and listYear[j] <= buy:
            listPrice.put(buy-listYear[j])
    i += 1

print(listPrice.get())