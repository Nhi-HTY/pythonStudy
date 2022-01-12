import queue

while True:
    try:
        n = int(input())
    except EOFError:
        break

    s = []
    q = queue.Queue()
    pq = queue.PriorityQueue()

    isStack = isQueue = isPriorityQueue = True

    for _ in range(n):
        inputData = list(map(int, input().split()))
        if inputData[0] == 1:
            s.append(inputData[1])
            q.put(inputData[1])
            pq.put(-inputData[1])
        elif inputData[0] == 2:
            if inputData[1] != s.pop():
                isStack = False
            if inputData[1] != q.get():
                isQueue = False
            if inputData[1] != -pq.get():
                isPriorityQueue = False

    if isStack + isQueue + isPriorityQueue == 0:
        print("impossible")
    elif isStack + isQueue + isPriorityQueue > 1:
        print("not sure")
    elif isStack:
        print("stack")
    elif isQueue:
        print("queue")
    else:
        print("priority queue")
