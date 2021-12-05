totalCard = int(input())
listCard = list(map(int, input().split()))

totalSeria = 0
totalDima = 0
step = 0

start = 0
end = len(listCard) - 1

if len(listCard) <= 1:
    totalSeria = listCard[0]
    totalDima = 0
else:
    while start <= end:
        if step % 2 == 0:
            if listCard[end] >= listCard[start]:
                totalSeria += listCard[end]
                end -= 1
            else:
                totalSeria += listCard[start]
                start += 1
            step += 1
        else:
            if listCard[end] >= listCard[start]:
                totalDima += listCard[end]
                end -= 1
            else:
                totalDima += listCard[start]
                start += 1
            step += 1

print(totalSeria, end=' ')
print(totalDima)
