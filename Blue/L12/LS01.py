def BinarySearch(x, left, right, listNum):
    while left <= right:
        mid = (right + left) // 2
        if (mid == left or x > listNum[mid - 1]) and listNum[mid] == x:
            return mid
        elif listNum[mid] < x:
            return BinarySearch(x, mid + 1, right, listNum)
        else:
            return BinarySearch(x, left, mid - 1, listNum)
    return -1

t = 0
while True:
    n, q = map(int, input().split())
    if n == 0 and q == 0:
        break
    t += 1
    a = []
    for _ in range(n):
        num = int(input())
        a.append(num)
    a.sort()
    left = 0
    right = len(a) - 1
    print("CASE# {}:".format(t))
    for j in range(q):
        query = int(input())
        pos = BinarySearch(query, left, right, a)
        print("{} found at {}".format(query, pos+1)) if pos != -1 else print("{} not found".format(query))

