import queue

maxHeap = queue.PriorityQueue()
minHeap = queue.PriorityQueue()
n = int(input())
total = 0
for _ in range(n):
    review = list(map(int, input().split()))
    if review[0] == 1:
        total += 1
        if not minHeap.empty() and review[1] > minHeap.queue[0]:
            maxHeap.put(-minHeap.get())
            minHeap.put(review[1])
        else:
            maxHeap.put(-review[1])
        if total % 3 == 0:
            minHeap.put(-maxHeap.get())
    else:
        if minHeap.empty():
            print("No reviews yet")
        else:
            print(minHeap.queue[0])