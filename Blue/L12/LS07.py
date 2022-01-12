n, k = map(int, input().split())
listNum = list(map(int, input().split()))
listNum.sort()
count = 0
for x in listNum:
    num = k + x
    l = 0
    r = len(listNum) - 1
    while l <= r:
        mid = (l + r) // 2
        if listNum[mid] == num:
            count += 1
            break
        elif listNum[mid] < num:
            l = mid + 1
        else:
            r = mid - 1

print(count)