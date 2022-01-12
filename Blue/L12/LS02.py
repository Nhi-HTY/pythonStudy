def BinarySearch(listMoney, left, right, x):
    if left <= right:
        mid = (left + right)//2
        if listMoney[mid] == x:
            return True
        elif listMoney[mid] < x:
            return BinarySearch(listMoney, left + 1, right, x)
        else:
            return BinarySearch(listMoney, left, right - 1, x)
    return False

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    line = list(map(int, input().split()))
    line.sort()
    count = 0
    while len(line) > 1:
        first = line.pop()
        second = m - first
        left = 0
        right = len(line) - 1
        isExist = BinarySearch(line, left, right, second)
        if isExist:
            count += 1
    print(count)

