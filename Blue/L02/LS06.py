n = int(input())
listData = list(map(int, input().split()))

start, end = 0, 1
minData = maxData = 0
maxRangeLen = 2
pointerMin = 0
pointerMax = 0

if listData[start] > listData[end]:
    minData = listData[end]
    pointerMin = end
    maxData = listData[start]
    pointerMax = start
else:
    minData = listData[start]
    pointerMin = start
    maxData = listData[end]
    pointerMax = end

while end <= n - 1:
    if listData[end] - 1 == minData or listData[end] + 1 == maxData:
        if listData[end] != listData[end-1]:
            if listData[end] - 1 == minData:
                maxData = listData[end]
                pointerMax = end
            if listData[end] + 1 == maxData:
                minData = listData[end]
                pointerMin = end
        maxRangeLen = max(maxRangeLen, end - start + 1)
        end += 1
    else:
        if listData[end] > maxData:
            start = pointerMax
            maxData = listData[end]
            minData = maxData - 1
        else:
            start = pointerMin
            minData = listData[end]
            maxData = minData + 1
print(maxRangeLen)

