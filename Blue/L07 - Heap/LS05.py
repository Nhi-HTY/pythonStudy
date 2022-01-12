import heapq
used = [False] * (10**6)

n = int(input())
minHeap = []
maxHeap = []
cost = 0
billNo = 1

for _ in range(n):
    receipt = list(map(int, input().split()))
    for i in range(1, receipt[0]+1):
        heapq.heappush(minHeap, (receipt[i], billNo))
        heapq.heappush(maxHeap, (-receipt[i], billNo))
        billNo += 1
    while used[minHeap[0][1]] == True:
        heapq.heappop(minHeap)
    while used[maxHeap[0][1]] == True:
        heapq.heappop(maxHeap)
    used[minHeap[0][1]] = True
    used[maxHeap[0][1]] = True
    largest = -heapq.heappop(maxHeap)[0]
    smallest = heapq.heappop(minHeap)[0]
    cost += largest - smallest
print(cost)